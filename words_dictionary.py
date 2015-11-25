import lda
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from langdetect import detect
from gensim import corpora, models 


def sites(path):
    f = open(path, 'r')
    row = f.readline()
    while row:
        row = row.split('|')
        site = row[3].strip('\n')
        pages = [[component.strip('()') for component in \
                  page.strip('()').split('~~')[1].strip('{}').strip('{}').split('~') if component] \
                  for page in site.strip('{}').split('~~~') if page]
        pages = [page for page in pages if page]
        pages = [[c for c in p if c ] for p in pages]
        site = dict(site_id=row[0], category=row[1], url=row[2], site=pages)
        yield site
        row = f.readline()
        

def get_words(text):
    if not text.decode('utf-8'):
        return None
    if not (detect(text.decode('utf-8')) == u'en'):
        print detect(text.decode('utf-8'))
        return None
    
    text = text.replace(r',./\“”!@#$%^&*()-\'"+=`~:;?><', ' ')
    words = [porter.stem(word) for word in word_tokenize(text)
             if word.isalpha()
             and len(word) >= 3
             and word not in stopwords.words('english')]
    return words


def make_word_dict(path, num_of_topict=200, passes=20):
    words_dict = dict()
    corpus = []
    dictionary = []
    i=0
    for title in sites(path):
        text = []
        for page in title['site']:
            for paragraph in page:
                if get_words(paragraph):
                    text += get_words(paragraph)
        article = corpora.Dictionary([text])
        dictionary.append(article)
        corpus.append(article.doc2bow(text))
        i+=1
        if i > 100:
            break
        
    ldamodel = models.ldamodel.LdaModel(corpus, num_topics=num_of_topict, id2word=dictionary, passes=passes)
    return ldamodel
        
            

# print(ldamodel.print_topics(num_topics=3, num_words=3))
# dictionary.token2id(0)
porter = PorterStemmer()
path = 'D:\DataHack\datahack_sitetext_train_final.csv'
num_of_topict = 300
passes = 20
ldamodel = make_word_dict(path, num_of_topict=num_of_topict, passes=passes)

print ldamodel.print_topics(num_topics=num_of_topict, num_words=3)
