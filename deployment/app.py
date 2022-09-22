from flask import Flask, request, render_template, redirect, url_for
from mypackages.ny_time.ny_time_output import data_output
from mypackages.ny_time.ny_time_cleasnig import text_cleansing
import pickle

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
       form_1 = request.form['nm']
       return redirect(url_for('model', article = form_1))
    else:
        return render_template("main.html")

@app.route("/result <article>")
def model(article):
    _text_cleasing = text_cleansing(article) 
    _cleansing_result = _text_cleasing.before_cleasing() 
    model = pickle.load(open('model.pkl', 'rb'))
    cv = pickle.load(open('cv.pkl', 'rb'))
    text = [_cleansing_result]
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
    return render_template('main.html', output=result)

@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        form_3 = request.form['test']
        return redirect(url_for('show_result', output=form_3))
    else:
        return render_template("test.html")

@app.route("/test <output>")
def show_result(output):
    _clean = text_cleansing(output)
    _clean_result = _clean.after_cleansing()
    return render_template('test.html', val=_clean_result)

@app.route('/visualization')
def hello():
    data = data_output(2021, 5)
    predict = data.get_values()
    return render_template('statics.html', data=predict)

if __name__ == '__main__':
    app.run(debug=True)
