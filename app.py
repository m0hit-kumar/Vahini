from flask import request
from flask import Flask
from flask import jsonify
# import numpy as np
# import string
# from nltk.corpus import stopwords
# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer
# from sklearn.pipeline import Pipeline
# # import pickle
import pickle

# test for ML

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # global model
    # model = pickle.load(open('model.pkl', 'rb'))
    return "<h1>Vahini Chatbot API</h1>"


@app.route("/ml/reply", methods=['GET'])
def reply():
    # ques = request.args.get('question', default="hello", type=str)
    # ques = [ques]
    # ans = model.predict(ques)[0]
    # return jsonify(reply=ans)
    return "< h1 > hi < /h1 >"
