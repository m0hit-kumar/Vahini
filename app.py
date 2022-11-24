from flask import request
from flask import Flask
import string
from flask import jsonify
import pickle
def cleaner(x):
    return [a for a in (''.join([a for a in x if a not in string.punctuation])).lower().split()]

app = Flask(__name__)


class CustomUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        try:
            return super().find_class(__name__, name)
        except AttributeError:
            return super().find_class(module, name)

model = CustomUnpickler(open('model.pkl', 'rb')).load()

@app.route('/', methods=['GET'])
def index():       
    return "<h1>Vahini Chatbot API</h1>"


@app.route("/ml/reply", methods=['GET'])
def reply():
    ques = request.args.get('question', default="hello", type=str)
    ques = [ques]
    ans = model.predict(ques)[0]
    return jsonify(reply=ans)
 