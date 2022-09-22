import json
import time
import requests
import datetime
import dateutil
import pandas as pd
from dateutil.relativedelta import relativedelta

def parse_response(year=2020, date=1):
    '''API request'''
    base_url = 'https://api.nytimes.com/svc/archive/v1'
    url = base_url + '/' + str(year) + '/' + str(date) + '.json?api-key=' + '3YIxSGJ8fF20rV8LAKKKPx05mNoB9AFl'
    response = requests.get(url).json()
    time.sleep(6)
    '''API parsing and turn into DataFrame'''
    data = {
        'date': [],
        'url' : [],
        'headline': [],  
        'articles' : [],
        'doc_type': [],
        'material_type': [],
        'section': [],
        'keywords': []
        }
    articles = response['response']['docs']
     
    for article in articles: # For each article, make sure it falls within our date range
        date = dateutil.parser.parse(article['pub_date']).date()
        data['date'].append(date)
        data['headline'].append(article['headline']['main']) 
        data['url'].append(article['web_url'])
        data['articles'].append(article['snippet'])
        if 'section' in article:
            data['section'].append(article['section_name'])
        else:
            data['section'].append(None)
        data['doc_type'].append(article['document_type'])
        if 'type_of_material' in article: 
            data['material_type'].append(article['type_of_material'])
        else:
            data['material_type'].append(None)
        keywords = [keyword['value'] for keyword in article['keywords'] if keyword['name'] == 'subject']
        data['keywords'].append(keywords)
    
    df = pd.DataFrame(data) 
    return df

if __name__ == '__main__':
    print(parse_response())