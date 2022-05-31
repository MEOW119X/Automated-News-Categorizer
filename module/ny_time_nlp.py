from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk import WordNetLemmatizer

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
    return [lemmatizer.lemmatize(x, 'v') if i.startswith('V') else lemmatizer.lemmatize(x, 'n') if i.startswith('N') else lemmatizer.lemmatize(x, 'a') if i.startswith('J') else lemmatizer.lemmatize(x, 'r') if i.startswith('R') else '' for x,i in row]

def join_words(row):
    """Join the text"""
    return " ".join(x for x in row)
