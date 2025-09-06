import streamlit as st
import joblib

tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
lr_model = joblib.load('sentiment_model.pkl')


# Streamlit UI
st.title("IMDB Movie Review Sentiment Analysis 🎬")
st.write("Enter a movie review below to predict whether it is Positive or Negative.")

# Text input
user_input = st.text_area("Enter Review:")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        # Transform input and predict
        input_vector = tfidf_vectorizer.transform([user_input])
        prediction = lr_model.predict(input_vector)[0]
        probability = lr_model.predict_proba(input_vector)[0].max()  # confidence score

        # Display result
        if prediction == 'positive':
            st.success(f"Sentiment: Positive 👍")
        else:
            st.error(f"Sentiment: Negative 👎 ")
