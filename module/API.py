import json
import time
import requests
import datetime
import dateutil
import pandas as pd
from dateutil.relativedelta import relativedelta

date = ['2020', '1']

def send_request(date):
    '''API request'''
    
    base_url = 'https://api.nytimes.com/svc/archive/v1'
    url = base_url + '/' + date[0] + '/' + date[1] + '.json?api-key=' + '3YIxSGJ8fF20rV8LAKKKPx05mNoB9AFl'
    response = requests.get(url).json()
    time.sleep(6)
    return response


def parse_response(response):
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
    return pd.DataFrame(data) 

def output():
    response = send_request(date)
    df = parse_response(response)
    return df

if __name__ == '__main__':
    print(output())