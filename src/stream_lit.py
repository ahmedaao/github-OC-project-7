# Import packages
import streamlit as st
import json
import requests


st.title("Sentiment Analysis for text")

# Summary of the app functionality
st.write(
    """This basic application is a POC (Proof Of Concept) which ask you to
    enter a sentence. Then, you will have the sentiment analysis of it
    (positive or not) as a output"""
)

# Taking user input text
text = st.text_input("Please, enter a sentence :")

st.write("")

# Converting the inputs into a json format
input = {"text": text}

# When the user clicks on button it will fetch the API
if st.button("Prediction"):
    res = requests.post(url="http://0.0.0.0:8000/predict", data=json.dumps(input))

    st.subheader(f"Response from API = {res.text}")
