import streamlit as st
import pickle
import re

model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
le = pickle.load(open('label_encoder.pkl', 'rb'))

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text.lower()

def predict_resume(text):
    cleaned = clean_text(text)
    vector = tfidf.transform([cleaned]).toarray()
    prediction = model.predict(vector)
    return le.inverse_transform(prediction)[0]

st.title("AI Resume Screening System")

text = st.text_area("Paste your resume here")

if st.button("Predict"):
    result = predict_resume(text)
    st.success(f"Predicted Category: {result}")
