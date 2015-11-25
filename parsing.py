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


