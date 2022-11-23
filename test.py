import pickle

m = pickle.load((open('./model.pkl','rb')))

# print(m)
print(m.predict('I want to tansfer money'))