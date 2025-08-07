# check pytest is going to broke first or me
def test_sanity():
    assert 1 + 1 == 2  # hate math


# main stuff
import pytest
from unittest.mock import MagicMock
import pandas as pd
from bug_model import train_classifier, evaluate_model
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier

def test_train_classifier_returns_multioutput():
    model = LogisticRegression()
    X = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
    y = [[1, 0], [0, 1], [1, 1]]

    clf = train_classifier(model, X, y)

    # :v
    assert isinstance(clf, MultiOutputClassifier)
    assert hasattr(clf, "predict")

def test_evaluate_model_prints_report(capsys):
    # tired
    fake_model = MagicMock()
    fake_model.predict.return_value = [[1, 0], [0, 1]]

    X_test = [[0.1, 0.2], [0.3, 0.4]]
    y_test = pd.DataFrame([[1, 0], [0, 1]], columns=["label", "severity"])
    cols = ["label", "severity"]

    evaluate_model(fake_model, X_test, y_test, cols)

    # what's printed
    out = capsys.readouterr().out
    assert "--- LABEL ---" in out
    assert "--- SEVERITY ---" in out