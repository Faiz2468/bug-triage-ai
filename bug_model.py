import numpy as np
from sklearn.multioutput import MultiOutputClassifier

# 🧠 Training function
def train_classifier(base_model, X_train, y_train):
    clf = MultiOutputClassifier(base_model)
    clf.fit(X_train, y_train)
    return clf

# 📊 Evaluation function
def evaluate_model(clf, X_test_emb, y_test, target_cols):
    from sklearn.metrics import classification_report
    y_pred = clf.predict(X_test_emb)
    y_pred = np.array(y_pred)  # ✅ Fix: convert list of lists to NumPy array

    print("📊 Evaluation:")
    for i, col in enumerate(target_cols):
        print(f"\n--- {col.upper()} ---")
        print(classification_report(y_test.iloc[:, i], y_pred[:, i]))