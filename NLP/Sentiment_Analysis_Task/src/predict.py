import joblib
import os
from preprocess import clean_text

def predict_sentiment(text):
    # 1. جلب المسار الديناميكي للمشروع
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 2. تجميع المسار الكامل لملفات الموديل
    model_path = os.path.join(BASE_DIR, 'models', 'sentiment_model.pkl')
    tfidf_path = os.path.join(BASE_DIR, 'models', 'tfidf_vectorizer.pkl')
    
    # Load the saved model and vectorizer
    try:
        model = joblib.load(model_path)
        tfidf = joblib.load(tfidf_path)
    except FileNotFoundError:
        print("Error: Model files not found. Please run train.py first.")
        return

    # Clean the input text using the same function
    cleaned = clean_text(text)
    
    # Vectorize the text
    vectorized = tfidf.transform([cleaned])
    
    # Predict
    prediction = model.predict(vectorized)[0]
    
    if prediction == 1:
        print(f"Review: '{text}' --> Sentiment: POSITIVE")
    else:
        print(f"Review: '{text}' --> Sentiment: NEGATIVE")

if __name__ == "__main__":
    # Test with some examples
    print("Testing predictions...\n")
    predict_sentiment("This product is completely useless, I hate it.")
    predict_sentiment("I am very happy with my purchase, amazing quality!")