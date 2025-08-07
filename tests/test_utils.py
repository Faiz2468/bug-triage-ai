# finally figured out the math
def test_math_sanity():
    assert 2 + 2 == 4

import pytest
import pandas as pd
from utils import clean_text, preprocess

# test if clean_text works
def test_clean_text_basic():
    text = "Hello, WORLD!   Welcome to AI.  "
    expected = "hello world welcome to ai"
    assert clean_text(text) == expected

# test when input is just symbols and garbage
def test_clean_text_only_special_chars():
    text = "@#$%^&*()!"
    expected = ""
    assert clean_text(text) == expected

# check if preprocess creates text column properly
def test_preprocess_creates_text_column():
    df = pd.DataFrame({
        'title': ['Bug 1', None],
        'description': ['App crashes', 'Null pointer exception']
    })
    processed = preprocess(df)
    assert 'text' in processed.columns
    assert processed.loc[0, 'text'] == "bug 1 app crashes"
    assert processed.loc[1, 'text'] == "null pointer exception"

# check if preprocess is smart enough
def test_preprocess_handles_missing_data():
    df = pd.DataFrame({
        'title': [None, None],
        'description': [None, "Test"]
    })
    processed = preprocess(df)
    assert processed.loc[0, 'text'] == ""
    assert processed.loc[1, 'text'] == "test"