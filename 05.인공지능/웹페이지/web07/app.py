from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, template_folder='temp', static_folder='static')


@app.route('/data')
def data():
    page = int(request.args['page'])
    size = int(request.args['size'])
    start = (page-1) * size #0, 5, 10
    end = (page*size) #4, 9, 14
    df = pd.read_csv('data/타이타닉/test.csv')
    cols = ['Name', 'Sex', 'Age', 'Fare', 'Pclass', 'Embarked']
    df = df[cols]
    df.columns = ['성명', '성별', '나이', '요금', '등석', '항구']
    total = len(df)
    df = df[start:end]
    table = df.to_html(classes='table table-striped table-dark table-hover', index=True)
    data = {'table':table, 'total':total}
    return data

@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='타이타닉 생존예측')


if __name__=='__main__':
    app.run(port=5000, debug=True)