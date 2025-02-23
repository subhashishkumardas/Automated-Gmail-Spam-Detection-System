# spam_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
import os

MODEL_PATH = "spam_model.pkl"

def train_spam_detector():
    # Load spam dataset
    data = pd.read_csv("data/spam.csv", encoding="latin-1")
    data = data.rename(columns={"v1": "label", "v2": "message"})
    data = data[["label", "message"]]
    data["label"] = data["label"].map({"spam": 1, "ham": 0})
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(data["message"], data["label"], test_size=0.2, random_state=42)
    
    # Create a pipeline that includes vectorization and model
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(model, MODEL_PATH)
    print("Spam detection model trained and saved.")

def load_spam_detector():
    if not os.path.exists(MODEL_PATH):
        train_spam_detector()
    return joblib.load(MODEL_PATH)

def is_spam(message):
    model = load_spam_detector()
    prediction = model.predict([message])
    return bool(prediction[0])  # Returns True if spam, False if not
