# 🎬 IMDB Sentiment Analysis

This project performs **sentiment analysis** on IMDB movie reviews using **Natural Language Processing (NLP)** and **Machine Learning** techniques.  
The goal is to classify reviews as **positive** or **negative** by applying text preprocessing, feature extraction, and machine learning classifiers.

---

## 🚀 Features
- Text Preprocessing (lowercasing, punctuation & number removal, stopword removal, spell correction, etc.)
- Feature Extraction:
  - Bag of Words (BoW)
  - TF-IDF
- Machine Learning Models:
  - Naive Bayes
  - Support Vector Machine (SVM)
  - Logistic Regression (best accuracy with TF-IDF + hyperparameter tuning)
- Model evaluation using accuracy scores
- Streamlit UI for easy interaction

---

📊 Results

Logistic Regression with TF-IDF features gave the highest accuracy.

Streamlit app allows users to input reviews and get real-time sentiment predictions.


📌 Future Improvements

Deploy model on cloud (Heroku/Streamlit Cloud)

Use Deep Learning (LSTM, Transformers)

Expand dataset for better generalization
