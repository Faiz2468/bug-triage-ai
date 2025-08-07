# bug-triage-ai

This project is an AI that can read bug reports and go:
> “okay this bug is serious, kinda urgent, and send it to team backend pls 😤”

basically it helps devs by tagging bugs automatically.

---

## what’s the point?

bugs are annoying. figuring out where it is also annoying.

so Imma use some machine learning tech:
- guess the **type**
- guess how **severe** it is
- guess the **priority**
- guess which **team** should fix it


---

## tools used

- `Python`
- `pandas` + `scikit-learn` for data & ML
- `sentence-transformers` (BERT, honestly I'm still clueless the full function of it, still learning)
- `MultiOutputClassifier` with `LogisticRegression`
- `joblib` to save
- `pytest` making sure nothing explodes
- `streamlit` to show off (optional 👀)

---

## how it supposed to work

1. `generate_bugs.py` → makes fake bug reports and saves `bugs.csv`
2. `bug_classifier.py` → processes data, evaluates it
3. `bug_model.py` → use ML logic (still messy)
4. `utils.py` → text cleaning, etc.
5. `app.py` → streamlit app for live prediction demo
6. `tests/` → testing the function works or not

### it predicts these:
- `label` → what kind of bug? (UI, Backend, etc)
- `severity` → how bad is it?
- `priority` → how fast do we fix this?
- `team` → who’s in charge?

---

## getting started

```bash
# clone it
git clone https://github.com/Faiz2468/bug-triage-ai.git
cd bug-triage-ai

# make the environment
python -m venv venv
venv\Scripts\activate   

# install all ingredients
pip install -r requirements.txt

# create some bugs
python data/generate_bugs.py

# train the brain
python bug_classifier.py

# run the UI
streamlit run app.py

## MIT licence
Do what u want. just don’t sell it
