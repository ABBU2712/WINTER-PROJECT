{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "import pandas as pd\n",
    "#from flasgger import Swagger\n",
    "import streamlit as st \n",
    "\n",
    "from PIL import Image\n",
    "\n",
    "#app=Flask(__name__)\n",
    "#Swagger(app)\n",
    "\n",
    "pickle_in = open(\"classifier.pkl\",\"rb\")\n",
    "classifier=pickle.load(pickle_in)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def welcome():\n",
    "    return \"Welcome All\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def predict_genre(danceability,energy,loudness,instrumentalness,valence,tempo):\n",
    "    prediction=classifier.predict([[danceability,energy,loudness,instrumentalness,valence,tempo]])\n",
    "    print(prediction)\n",
    "    return prediction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    st.title(\"DISCOVER YOUR GENRE\")\n",
    "    html_temp = \"\"\"\n",
    "    <div style=\"background-color:tomato;padding:10px\">\n",
    "    <h2 style=\"color:white;text-align:center;\">Streamlit song genre classifier ML App </h2>\n",
    "    </div>\n",
    "    \"\"\"\n",
    "    st.markdown(html_temp,unsafe_allow_html=True)\n",
    "    danceability = st.text_input(\"DANCEABILITY\",\"Type Here on a scale of 1-100 how much you feel like dancing on this song\")\n",
    "    energy = st.text_input(\"ENERGY\",\"Type Here your josh on a scale of 1-100\")\n",
    "    loudness = st.text_input(\"LOUDNESS\",\"Type Here the rate at which your heart starts shaking on a scale of 1-100\")\n",
    "    instrumentalness = st.text_input(\"INSTRUMENTALNESS\",\"Type Here what you feel like the use of instruments in this song on a scale of 1-100\")\n",
    "    valence = st.text_input(\"VALENCE\",\"Type Here the musical positiveness conveyed by the song on a scale of 1-100\")\n",
    "    tempo = st.text_input(\"TEMPO\",\"Type Here the tic tacness / speed of the  song pn a scale of 1-100\")\n",
    "    result=\"\"\n",
    "    if st.button(\"Predict\"):\n",
    "        result=predict_genre(danceability,energy,loudness,instrumentalness,valence,tempo)\n",
    "    st.success('The output is {}'.format(result))\n",
    "    if st.button(\"About\"):\n",
    "        st.text(\"Lets LEarn\")\n",
    "        st.text(\"Built with Streamlit\")\n",
    "\n",
    "if __name__=='__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
