from datetime import date
import re
from mypackages.ny_time.ny_time_api import parse_response
from mypackages.ny_time.ny_time_cleasnig import remove_special_char, join_words, extract_label, nan_remover, lowercase,  stop_word, pos_taggin, words_lemmatize, text_cleansing, apply_text
from mypackages.ny_time.ny_time_eda import count_values
import pickle
model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('cv.pkl', 'rb'))

class data_output:
    def __init__(self,years, date):
        self.date = date
        self.years = years
    

    def get_values(self): 
        df = parse_response(self.years, self.date)
        df['label'] = extract_label(df)
        df['articles'] = df['articles'].apply(apply_text)
        df = nan_remover(df)
        return df
      
    def predict(self):
        df = self.get_values()
        result = []
        for i in df['articles']:
            text = [i]
            yy = cv.transform(text)
            yy_pred = model.predict(yy)
            if yy_pred == 0:
                result.append('Opinion')
            if yy_pred == 1:
                result.append('World')
            if yy_pred == 2:
                result.append('Politics News')
            if yy_pred == 3:
                result.append('Arts')
            if yy_pred == 4:
                result.append('Business')
            else:
                result.append('Sports')
        return result
    
if __name__ == '__main__':
    df = data_output(2021, 5)
    api = df.get_values()
    # predict = df.pridict()
    api.to_csv('precessed.csv')
    print(api)
    
