#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


# In[2]:


def welcome():
    return "Welcome All"


# In[6]:


def predict_genre(danceability,energy,loudness,instrumentalness,valence,tempo):
    prediction=classifier.predict([[danceability,energy,loudness,instrumentalness,valence,tempo]])
    print(prediction)
    return prediction


# In[12]:


def main():
    st.title("DISCOVER YOUR GENRE")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit song genre classifier ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    danceability = st.text_input("DANCEABILITY","Type Here on a scale of 1-100 how much you feel like dancing on this song")
    energy = st.text_input("ENERGY","Type Here your josh on a scale of 1-100")
    loudness = st.text_input("LOUDNESS","Type Here the rate at which your heart starts shaking on a scale of 1-100")
    instrumentalness = st.text_input("INSTRUMENTALNESS","Type Here what you feel like the use of instruments in this song on a scale of 1-100")
    valence = st.text_input("VALENCE","Type Here the musical positiveness conveyed by the song on a scale of 1-100")
    tempo = st.text_input("TEMPO","Type Here the tic tacness / speed of the  song pn a scale of 1-100")
    result=""
    if st.button("Predict"):
        result=predict_genre(danceability,energy,loudness,instrumentalness,valence,tempo)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()


# In[ ]:




