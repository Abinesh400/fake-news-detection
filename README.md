# 📰 Advanced Fake News Detection Using Natural Language Processing

This project is an AI-powered solution for detecting fake news articles using Natural Language Processing (NLP) and Machine Learning. It uses logistic regression with TF-IDF features to classify news text as either **real** or **fake**.

---

## 🚀 Features

- Preprocessing of raw text (cleaning, stopword removal)
- TF-IDF vectorization of cleaned news content
- Logistic Regression model for binary classification
- Accuracy > 95% on test set
- Streamlit app to interact with the model

---

## 📂 Project Structure

fake-news-detector/
├── fake_news_app.py # Streamlit UI
├── fake_news_model.pkl # Trained ML model
├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer
├── Fake_News_Detection_NLP.ipynb # Colab notebook with full workflow
├── requirements.txt # Python dependencies
└── README.md


---

## 🧠 Model Details

- **Vectorization**: TF-IDF with 5000 max features
- **Classifier**: Logistic Regression
- **Dataset**: [Fake and Real News Dataset on Kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
- **Performance**:
  - Accuracy: ~96%
  - Precision/Recall: Evaluated on 20% test split

---

## 🛠️ How to Run

### 🔧 Local Setup

1. Clone the repo:
   
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector


2. Install dependencies:

pip install -r requirements.txt


3. Run the Streamlit app:

streamlit run fake_news_app.py
