import re
import nltk
from nltk.corpus import stopwords

# Download stopwords list if not already downloaded
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """
    Cleans text by lowercasing, removing special characters, and removing stopwords.
    """
    # Convert to string to avoid errors with NaN or numbers
    text = str(text)
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove special characters, punctuation, and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Remove stopwords
    text = " ".join([word for word in text.split() if word not in stop_words])
    
    return text