# Amazon Reviews Sentiment Analysis 📊

A complete Natural Language Processing (NLP) pipeline to classify Amazon product reviews into positive and negative sentiments. This project demonstrates end-to-end Machine Learning practices, from raw data preprocessing to deploying a trained model for predictions.

## 🚀 Features

*   **Robust Text Preprocessing:** Custom pipeline to clean text, remove special characters, and filter out English stopwords.
*   **Feature Engineering:** Utilizes `TfidfVectorizer` to transform text data into numerical format for machine learning models.
*   **Handling Imbalanced Data:** Implements `class_weight='balanced'` in Logistic Regression to accurately detect minority classes (negative reviews).
*   **Model Comparison:** Benchmarks Logistic Regression against Multinomial Naive Bayes.
*   **Data Visualization:** Generates WordClouds to visually represent the most frequent words in positive and negative reviews.
*   **Production-Ready Structure:** Clean, modularized code separated into source scripts (`src/`) and saved model artifacts (`models/`).

## 📁 Project Structure

```text
Sentiment_Analysis_Task/
│
├── data/                      
│   ├── raw/                   # Raw Amazon reviews dataset
│   └── processed/             # Cleaned dataset (optional)
│
├── models/                    # Saved model artifacts (.pkl)
│   ├── sentiment_model.pkl    
│   └── tfidf_vectorizer.pkl   
│
├── notebooks/                 
│   └── explorations_and_training.ipynb  # EDA, model training, and WordCloud generation
│
├── src/                       # Source code for the pipeline
│   ├── preprocess.py          # Text cleaning module
│   ├── train.py               # Script to train and save the model
│   └── predict.py             # Script to load the model and make new predictions
│
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

📈 Results Overview
The model achieves a balanced accuracy of ~92%, successfully identifying both positive and negative sentiments despite the initial class imbalance in the dataset.

## 📊 Data Visualizations

To visualize the model's logic, we generated WordClouds representing the top 100 words for each sentiment category:

### Positive Sentiment
![Positive WordCloud](reports/plots/positive_wordcloud.png)

### Negative Sentiment
![Negative WordCloud](reports/plots/negative_wordcloud.png)

👨‍💻 Author
Ahmed Abdelnaby Ali