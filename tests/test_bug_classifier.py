import pytest
from unittest.mock import MagicMock
import pandas as pd
from bug_classifier import train_classifier, evaluate_model
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier

def test_train_classifier_returns_multioutput():
    base_model = LogisticRegression()
    X = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
    y = [[1, 0], [0, 1], [1, 1]]

    clf = train_classifier(base_model, X, y)

    assert isinstance(clf, MultiOutputClassifier)
    assert hasattr(clf, "predict")

def test_evaluate_model_prints_report(capsys):
    mock_clf = MagicMock()
    mock_clf.predict.return_value = [[1, 0], [0, 1]]

    X_test_emb = [[0.1, 0.2], [0.3, 0.4]]
    y_test = pd.DataFrame([[1, 0], [0, 1]], columns=["label", "severity"])
    target_cols = ["label", "severity"]

    evaluate_model(mock_clf, X_test_emb, y_test, target_cols)

    output = capsys.readouterr().out
    assert "--- LABEL ---" in output
    assert "--- SEVERITY ---" in output