from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    model = pickle.load(open('model.pkl', 'rb'))
    cv = pickle.load(open('cv.pkl', 'rb'))
    text = [request.form.values()]
    cv_text = cv.transform(text)
    yy = model.predict(cv_text)
    result = ""
    if yy == [0]:
        result = "opinion"
    elif yy == [1]:
        result = "world"
    elif yy == [2]:
        result = "Politics News"
    elif yy == [3]:
        result = "arts"
    elif yy == [4]:
        result = "business"
    elif yy == [5]:
        result = "sports"
    return render_template('main.html', output=result )

if __name__ == '__main__':
    app.run(debug=True)

