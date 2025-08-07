import numpy as np
from sklearn.multioutput import MultiOutputClassifier

# train model
def train_classifier(base_model, X_train, y_train):
    multi_clf = MultiOutputClassifier(base_model)
    multi_clf.fit(X_train, y_train)
    return multi_clf  # hopefully now no issue

# check model again
def evaluate_model(clf, X_test_emb, y_test, target_cols):
    from sklearn.metrics import classification_report

    y_pred = clf.predict(X_test_emb)
    y_pred = np.array(y_pred)  # meh

    print("umm here's how it did i guess:")
    for i, col in enumerate(target_cols):
        print(f"\n--- {col.upper()} ---")
        print(classification_report(y_test.iloc[:, i], y_pred[:, i]))