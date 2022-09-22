from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk import WordNetLemmatizer
import pandas as pd
import numpy as np

def extract_label(df, x='url'):
    '''extract lebels from url'''
    df[x] = df[x].str.replace(r'(https?:\/\/www.nytimes.com\/(interactive)\/\d+\/\d+\/\d+\/)','', regex=True)
    df[x] = df[x].str.replace(r'(https?:\/\/www.nytimes.com\/\d+\/\d+\/\d+\/)','', regex=True)
    df[x] = df[x].str.replace(r'(https?:\/\/www.nytimes.com\/(slideshow)\/\d+\/\d+\/\d+\/)','', regex=True)
    df[x] = df[x].str.replace(r'(https?:\/\/www.nytimes.com\/(interactive)\/\d+\/)','', regex=True)
    df[x] = df[x].str.replace(r'(https?:\/\/www.nytimes.com\/(video)\/)','', regex=True)
    df[x] = df[x].str.replace(r'(https?:\/\/www.nytimes.com\/)','', regex=True)
    df[x] = df[x].str.replace(r'(https?:\/\/brandedplaylist.nytimes.com\/)','', regex=True)
    df[x] = df[x].str.replace(r'((us)\/)','', regex=True)
    df[x] = df[x].str.replace(r'(\/.+)','', regex=True)
    df[x] = df[x].str.replace(r'\s+','', regex=True)
    df[x] = df[x].str.replace(r'(.+(.html))','us', regex=True)
    return df[x]

def nan_remover(df):
    ind = df.loc[df['articles'] == ''].replace(np.nan, '').index
    df = df.drop(index=ind)
    return df

def lowercase(row):
    """Lowercase the text"""
    return row.lower()

def remove_special_char(row):
    """Remove the special characters from the text 
       and return into string"""
    text =" "
    for i in row:
        if i.isalnum():
            text+=i
        else:
            text+=' '
    return word_tokenize(text)

def stop_word(row):
    """Remove stop words from the text and return into list"""
    stop_words = set(stopwords.words('english'))
    return [x for x in row if x not in stop_words]

def pos_taggin(row):
    """put in nltk pos_tag into the text"""
    return pos_tag(row)

def words_lemmatize(row):
    """lemmatize the text with pos_tag"""
    lemmatizer = WordNetLemmatizer()  
    return [lemmatizer.lemmatize(x, 'v') 
            if i.startswith('V') 
            else lemmatizer.lemmatize(x, 'n') 
            if i.startswith('N') 
            else lemmatizer.lemmatize(x, 'a') 
            if i.startswith('J') 
            else lemmatizer.lemmatize(x, 'r') 
            if i.startswith('R') 
            else '' 
            for x,i in row]

def join_words(row):
    """Join the text"""
    return " ".join(x for x in row)

class text_cleansing():
    def __init__(self, text):
        self.text = text

    def before_cleasing(self):
        """Clean the text"""
        text = self.text
        text = text.lower()
        text = remove_special_char(text)
        text = pos_taggin(text)
        text = words_lemmatize(text)
        text = stop_word(text)
        text = join_words(text)
        return text

    def after_cleansing(self):
        '''Join the text'''
        text = self.before_cleasing()
        text = word_tokenize(text)
        text = join_words(text)
        return text

def apply_text(text):
    text_in = text_cleansing(text)
    return text_in.after_cleansing()

if __name__ == '__main__':
    text = """
              Former deputy prime minister Somkid Jatusripitak has accepted an invitation to serve as 
              a prime ministerial candidate of the newly established Sang Anakhot Thai Party (Building Thailand's Future).


              Party secretary-general Sontirat Sontijirawong said on Sunday Mr Somkid is willing to be 
              the candidate after he was approached for the role.
              
              "But it is still too early to officially announce a candidate for prime minister because 
              it is still not known when the election will be held. Other parties have not declared their candidates yet either," Mr Sontirat said.
              """

    text_clean = text_cleansing(text)
    text = text_clean.after_cleansing()
    print(text)