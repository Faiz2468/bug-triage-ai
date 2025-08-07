import re
import pandas as pd

# makes everything lowercase and removes weird symbols
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  
    text = re.sub(r'\s+', ' ', text).strip()  
    return text

# fix missing stuff
def preprocess(df):
    df['title'] = df['title'].fillna('')
    df['description'] = df['description'].fillna('')

    df['text'] = df['title'] + ' ' + df['description']
    df['text'] = df['text'].apply(clean_text)

    return df