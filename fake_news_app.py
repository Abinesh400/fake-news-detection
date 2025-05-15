import streamlit as st
import pickle
import string
import nltk

# Load model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Text cleaning function
def clean_text(text):
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    text = text.lower()
    text = ''.join([ch for ch in text if ch not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

# Streamlit UI
st.title("📰 Fake News Detector")
st.write("Enter a news article or paragraph below to predict if it's real or fake.")

input_text = st.text_area("Enter News Content Here")

if st.button("Predict"):
    if input_text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        cleaned = clean_text(input_text)
        vect_text = vectorizer.transform([cleaned]).toarray()
        prediction = model.predict(vect_text)[0]
        if prediction == 1:
            st.success("✅ This news is likely **Real**.")
        else:
            st.error("❌ This news is likely **Fake**.")
