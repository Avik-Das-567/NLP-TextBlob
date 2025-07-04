import streamlit as st
from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Sentiment Analysis
text = "I love learning Python!"
blob = TextBlob(text)
st.header("Sentiment Analysis")
st.subheader("Input Text :-", text)
st.subheader("Output :-", blob.sentiment)

# Tokenization
blob = TextBlob("Natural Language Processing is fun.")
st.header("Tokenization")
st.write("Input Text :- Natural Language Processing is fun.")
st.write("Words :-", blob.words)
st.write("Sentences :-", blob.sentences)

# POS Tagging
blob = TextBlob("Python is a powerful language")
st.header("POS Tagging")
st.write("Input Text :- Python is a powerful language")
st.write("Output :-", blob.tags)
