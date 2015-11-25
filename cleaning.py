from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()

def get_words(text):
    text = text.replace(r',./\“”!@#$%^&*()-\'"+=`~:;?><', ' ')
    words = [porter.stem(word) for word in word_tokenize(text)
             if word.isalpha()
             and len(word) >= 3
             and word not in stopwords.words('english')]
    return words




def clean_default_components(site):
    DEFAULTS = ['​click here to edit me', 'click here to add your own text and edit me',
                'use this area to describe one of your services',
                'use this area to let your visitors know about your latest news',
                'use this area to tell a story and let your users know a little more about you',
                'double click the image and choose from 100s of free images',
                'Add your own images by clicking on the gallery and',
                'Click to edit me and add text that says something nice',
                "an image title",
                'if you want to delete me just click on me and press delete',
                'proudly created with Wix.com',
                'Terry Francois Street',
                'great place to include more information about your',
                'great place to add more details about your product',
                'great space to write what makes',
                'great place to add more details about your product',
                'a menu title',
                'a menu section',
                ]
    pass


