import pandas as pb


def extract_label(x):
    '''To extract label in url'''
    url[x] = url[x].str.replace(r'(https?:\/\/www.nytimes.com\/(interactive)\/\d+\/\d+\/\d+\/)','', regex=True)
    url[x] = url[x].str.replace(r'(https?:\/\/www.nytimes.com\/\d+\/\d+\/\d+\/)','', regex=True)
    url[x] = url[x].str.replace(r'(https?:\/\/www.nytimes.com\/(slideshow)\/\d+\/\d+\/\d+\/)','', regex=True)
    url[x] = url[x].str.replace(r'(https?:\/\/www.nytimes.com\/(interactive)\/\d+\/)','', regex=True)
    url[x] = url[x].str.replace(r'(https?:\/\/www.nytimes.com\/(video)\/)','', regex=True)
    url[x] = url[x].str.replace(r'(https?:\/\/www.nytimes.com\/)','', regex=True)
    url[x] = url[x].str.replace(r'(https?:\/\/brandedplaylist.nytimes.com\/)','', regex=True)
    url[x] = url[x].str.replace(r'((us)\/)','', regex=True)
    url[x] = url[x].str.replace(r'(\/.+)','', regex=True)
    url[x] = url[x].str.replace(r'\s+','', regex=True)
    url[x] = url[x].str.replace(r'(.+(.html))','us', regex=True)
    return url.to_csv(r'X:\Code\Data\Thesis Automated News Catagorizing\virtualenvx\Automated-News-Categorizer\data\cleaned\label 2020.01.csv', index=False)


extract_label('url')

