import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Import the cleaning function from our preprocess.py module
from preprocess import clean_text

def main():
    print("Loading data...")
    
    # 1. جلب المسار الديناميكي للمشروع
    # __file__ بيجيب مسار ملف train.py الحالي
    # os.path.dirname بنستخدمها مرتين عشان نرجع خطوتين ورا (من src إلى فولدر المشروع الرئيسي)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 2. تجميع المسار الكامل لملف الداتا
    data_path = os.path.join(BASE_DIR, 'data', 'raw', 'amazon_reviews.csv')
    
    # 3. قراءة البيانات
    df = pd.read_csv(data_path)
    
    # Keep only relevant columns and drop NaNs
    df = df[['reviews.text', 'reviews.rating']].dropna()
    
    # Create binary sentiment (drop neutral 3s)
    df = df[df['reviews.rating'] != 3.0]
    df['sentiment'] = np.where(df['reviews.rating'] > 3.0, 1, 0)
    
    print("Cleaning text...")
    df['cleaned_text'] = df['reviews.text'].apply(clean_text)
    
    # Prepare features and target
    X = df['cleaned_text'].values
    y = df['sentiment'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Vectorizing text...")
    tfidf = TfidfVectorizer(max_features=5000)
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)
    
    print("Training Logistic Regression model...")
    model = LogisticRegression(max_iter=1000, class_weight='balanced')
    model.fit(X_train_tfidf, y_train)
    
    print("Evaluating model...")
    y_pred = model.predict(X_test_tfidf)
    print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    print(classification_report(y_test, y_pred))
    
    # --- SAVING THE MODEL AND VECTORIZER ---
    print("Saving model and vectorizer...")
    
    # تجميع المسار الكامل لفولدر models
    models_dir = os.path.join(BASE_DIR, 'models')
    os.makedirs(models_dir, exist_ok=True)
    
    joblib.dump(model, os.path.join(models_dir, 'sentiment_model.pkl'))
    joblib.dump(tfidf, os.path.join(models_dir, 'tfidf_vectorizer.pkl'))
    print("Saved successfully in 'models/' folder!")

if __name__ == "__main__":
    main()