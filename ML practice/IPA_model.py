#!/usr/bin/env python
# coding: utf-8

# In[145]:


from flask import Flask, request
import pickle
import numpy as np
import sys
import os
from flask_restful import Api, Resource, reqparse


# In[146]:


app = Flask(__name__)
api = Api(app)


# In[147]:


with open('rfc_model.pkl', 'rb') as rfc_model_pkl:
    rfc = pickle.load(rfc_model_pkl)


# In[148]:


with open('cbc_model.pkl', 'rb') as cbc_model_pkl:
    cbc = pickle.load(cbc_model_pkl)


# In[149]:


with open('gbc_model.pkl', 'rb') as gbc_model_pkl:
    gbc = pickle.load(gbc_model_pkl)


# In[150]:


with open('lgr_model.pkl', 'rb') as lgr_model_pkl:
    lgr = pickle.load(lgr_model_pkl)


# In[151]:


print(rfc)
print(cbc)
print(gbc)
print(lgr)


# In[152]:


fields = {'field1': {'field': 'age'}, 'field2': {'field': 'education-num'},}


# In[153]:


def abort_if_lgr_doesnt_exist(lgr_model):
    if lgr_model not in fields:
        abort(404, message="Fields {} doesn't exist".format(lgr_model))


# In[154]:


def abort_if_rfc_doesnt_exist(rfc_model):
    if rfc_model not in fields:
        abort(404, message="Fields {} doesn't exist".format(rfc_model))


# In[155]:


def abort_if_cbc_doesnt_exist(cbc_model):
    if cbc_model not in fields:
        abort(404, message="Fields {} doesn't exist".format(cbc_model))


# In[156]:


def abort_if_gbc_doesnt_exist(gbc_model):
    if gbc_model not in fields:
        abort(404, message="Fields {} doesn't exist".format(gbc_model))


# In[157]:


parser = reqparse.RequestParser()
parser.add_argument('field')


# In[158]:


#port = int(os.environ.get('PORT', 5000))


# In[159]:


@app.route('/')
def prediction():
    age = request.args.get('age')
    education_num = request.args.get('education-num')
    new_record = np.array([[age,education_num]])
    predict_result = knn.predict(new_record)
    return 'Predicted result for observation ' + str(new_record) + ' is: ' + str(predict_result)


# In[160]:


if __name__ == '__main__':
    app.run(debug = True)


# In[ ]:




