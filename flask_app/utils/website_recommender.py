#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np

st.title('Steam Game Recommendations')

col1, col2, col3 = st.columns([1,2,1])
with col2:
    with st.form(key='autenticacao'):
        input_login = st.text_input(label='Username')
        input_senha = st.text_input(label='Password',type="password")
        input_botao = st.form_submit_button('Login')
        
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

data = load_data(10000)

st.subheader('Random Data')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
