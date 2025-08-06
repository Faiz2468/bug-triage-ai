import re
import pandas as pd

def clean_text(text):
    """
    Lowercases, removes special characters, and extra spaces from text.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra whitespace
    return text

def preprocess(df):
    """
    Preprocesses a DataFrame by cleaning and combining title and description.
    """
    # Fill NaNs with empty strings
    df['title'] = df['title'].fillna('')
    df['description'] = df['description'].fillna('')

    # Combine and clean text
    df['text'] = df['title'] + " " + df['description']
    df['text'] = df['text'].apply(clean_text)

    return df