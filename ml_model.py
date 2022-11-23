import numpy as np 
import string
from nltk.corpus import stopwords
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer
from sklearn.pipeline import Pipeline
import pickle


df = pd.read_csv('./dialogs.txt',sep='\t')

df.columns=['Questions','Answers']


# Cleaning Dataset
def cleaner(x):
    return [a for a in (''.join([a for a in x if a not in string.punctuation])).lower().split()]

Pipe = Pipeline([
    ('bow',CountVectorizer(analyzer=cleaner)),
    ('tfidf',TfidfTransformer()),
    ('classifier',DecisionTreeClassifier())
])

Pipe.fit(df['Questions'],df['Answers'])

pickle.dump(Pipe,open('model.pkl','wb'))
# print(Pipe.predict(['Ritik Raj'])[0])