import streamlit as st
import joblib

# Load the model
model = joblib.load("model.pkl")  # Rename the file from 'model (1).pkl' to 'model.pkl' for convenience

# App UI
st.title("📷 HD Camera Review Sentiment Analysis")

review = st.text_area("Enter an HD camera review for sentiment analysis:")

if st.button("Analyze Sentiment"):
    if not review.strip():
        st.warning("Please enter a valid review.")
    else:
        prediction = model.predict([review])[0]
        st.success(f"🔍 Predicted Sentiment: **{prediction}**")
