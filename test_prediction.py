import pytest
import pandas as pd
import numpy as np
from utils import preprocess
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import LabelEncoder

# testing
@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'title': ['Login error', 'Crash on startup'],
        'description': ['User cannot login with valid credentials', 'App crashes when opened'],
        'label': ['Authentication', 'Crash'],
        'severity': ['High', 'Critical'],
        'priority': ['P1', 'P0'],
        'team': ['Backend', 'Frontend']
    })

# column added after
def test_preprocessing_adds_text_column(sample_data):
    df = preprocess(sample_data.copy())
    assert 'text' in df.columns
    assert df['text'].str.contains('login', case=False).any()

# testing label encoders and classifier shape
def test_encoding_and_prediction_shape(sample_data):
    df = preprocess(sample_data.copy())
    df['text'] = df['title'] + " " + df['description']
    target_cols = ['label', 'severity', 'priority', 'team']

    # encode each target col
    label_encoders = {}
    for col in target_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    X = df['text']
    y = df[target_cols]

    # BERT (mom's choice :v)
    X_emb = np.random.rand(len(X), 384)

    clf = MultiOutputClassifier(LogisticRegression(max_iter=1000))
    clf.fit(X_emb, y)
    y_pred = clf.predict(X_emb)

    assert y_pred.shape == y.shape