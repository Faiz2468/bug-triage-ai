# 🐞 Bug Triage AI

An intelligent multi-label classification system that predicts the **type**, **severity**, **priority**, and **responsible team** for incoming software bug reports using **BERT embeddings** and **multi-output logistic regression**.

---

## 🎯 Project Goal

To automate and streamline the bug triaging process using NLP and machine learning — enabling faster issue routing, reduced manual labeling, and smarter bug management.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**, **scikit-learn**
- **SentenceTransformers** (`all-MiniLM-L6-v2`)
- **MultiOutput Logistic Regression**
- **joblib** for model saving
- **pytest** for testing and validation
- **Streamlit** for the web-based interface (optional)

---

## ⚙️ How It Works

1. `generate_bugs.py`: Generates synthetic bug reports → `bugs.csv`
2. `bug_classifier.py`: Preprocess → Encode → Train → Evaluate → Save model
3. `bug_model.py`: Clean ML logic for training and evaluation (importable + testable)
4. `utils.py`: Handles text cleaning and merging bug fields
5. `app.py`: (Optional) Streamlit frontend for trying predictions
6. `tests/`: Pytest-based unit test suite for utility and model logic

### Labels Predicted:
- `label`: Type of bug (e.g., Authentication, UI, Performance)
- `severity`: How serious it is
- `priority`: Urgency level
- `team`: Responsible team

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/bug-triage-ai.git
cd bug-triage-ai

# 2. Set up virtual environment
python -m venv venv
venv\Scripts\activate        # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate data
python data/generate_bugs.py

# 5. Train the model
python bug_classifier.py

# 6. (Optional) Run Streamlit app
streamlit run app.py