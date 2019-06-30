import requests
from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    news_list = requests.get("http://127.0.0.1:8000/news/")
    news_list = news_list.json()

    categories = requests.get ("http://127.0.0.1:8000/category/")
    categories = categories.json()

    return render_template('index.html', news_list=news_list, categories=categories)