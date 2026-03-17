# ai-resume-screening-system
AI-powered Resume Screening System using Machine Learning and NLP. Classifies resumes into job roles with 99% accuracy and includes a Streamlit web app for real-time predictions.
# 🚀 AI Resume Screening System

## 📌 Overview

The **AI Resume Screening System** is a Machine Learning and Natural Language Processing (NLP) project that automatically classifies resumes into different job categories.

This project helps automate the recruitment process by analyzing resume content and predicting the most relevant job role.

---

## 🎯 Features

* Resume classification using NLP
* Text preprocessing and cleaning
* TF-IDF feature extraction
* Machine Learning model (Random Forest)
* High accuracy (~99%)
* Interactive web application using Streamlit

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* NLTK
* Streamlit

---

## 📊 Model Performance

* **Model:** Random Forest Classifier
* **Accuracy:** 99.48%
* **Vectorization:** TF-IDF (with n-grams)

---

## ⚙️ How It Works

1. User enters resume text in the app
2. Text is cleaned and preprocessed
3. TF-IDF converts text into numerical features
4. Model predicts the job category
5. Result is displayed instantly

---

## ▶️ How to Run

### Install dependencies

pip install pandas numpy scikit-learn nltk streamlit

### Run the app

streamlit run app.py

---

## 📁 Project Structure

resume-screening-ai/
│── app.py
│── model.pkl
│── tfidf.pkl
│── label_encoder.pkl
│── resume_project.ipynb
│── README.md

---

## 💡 Future Improvements

* Add PDF resume upload
* Use advanced NLP models like BERT
* Deploy on cloud (AWS / Render)
* Add resume scoring system

---

## ⭐ Conclusion

This project demonstrates how Machine Learning and NLP can be applied to real-world recruitment systems, making it a strong portfolio project for data science roles.

