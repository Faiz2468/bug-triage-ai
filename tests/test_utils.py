# ✅ This is a basic test to confirm pytest works
def test_math_sanity():
    assert 2 + 2 == 4

# ✅ These are your actual utility function tests
import pytest
import pandas as pd
from utils import clean_text, preprocess

def test_clean_text_basic():
    result = clean_text("Hello, WORLD!   Welcome to AI.  ")
    expected = "hello world welcome to ai"
    assert result == expected

def test_clean_text_only_special_chars():
    result = clean_text("@#$%^&*()!")
    expected = ""
    assert result == expected

def test_preprocess_creates_text_column():
    df = pd.DataFrame({
        'title': ['Bug 1', None],
        'description': ['App crashes', 'Null pointer exception']
    })
    processed = preprocess(df)
    assert 'text' in processed.columns
    assert processed.loc[0, 'text'] == "bug 1 app crashes"
    assert processed.loc[1, 'text'] == "null pointer exception"

def test_preprocess_handles_missing_data():
    df = pd.DataFrame({
        'title': [None, None],
        'description': [None, "Test"]
    })
    processed = preprocess(df)
    assert processed.loc[0, 'text'] == ""
    assert processed.loc[1, 'text'] == "test"