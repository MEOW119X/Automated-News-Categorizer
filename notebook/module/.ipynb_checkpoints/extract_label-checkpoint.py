import pandas as pd

def extract_label(df, url):
    '''To extract label in url'''
    df[url] = df[url].str.replace(r'(https?:\/\/www.nytimes.com\/(interactive)\/\d+\/\d+\/\d+\/)','', regex=True)
    df[url] = df[url].str.replace(r'(https?:\/\/www.nytimes.com\/\d+\/\d+\/\d+\/)','', regex=True)
    df[url] = df[url].str.replace(r'(https?:\/\/www.nytimes.com\/(slideshow)\/\d+\/\d+\/\d+\/)','', regex=True)
    df[url] = df[url].str.replace(r'(https?:\/\/www.nytimes.com\/(interactive)\/\d+\/)','', regex=True)
    df[url] = df[url].str.replace(r'(https?:\/\/www.nytimes.com\/(video)\/)','', regex=True)
    df[url] = df[url].str.replace(r'(https?:\/\/www.nytimes.com\/)','', regex=True)
    df[url] = df[url].str.replace(r'(https?:\/\/brandedplaylist.nytimes.com\/)','', regex=True)
    df[url] = df[url].str.replace(r'((us)\/)','', regex=True)
    df[url] = df[url].str.replace(r'(\/.+)','', regex=True)
    df[url] = df[url].str.replace(r'\s+','', regex=True)
    df[url] = df[url].str.replace(r'(.+(.html))','us', regex=True)
    return df[url]



