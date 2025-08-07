import streamlit as st
import pandas as pd
import joblib
from sentence_transformers import SentenceTransformer
from utils import preprocess

# loading for the #91 attempts hope this finally works
if 'model' not in st.session_state:
    st.session_state.model = joblib.load("models/classifier_multi.pkl")

if 'embedder' not in st.session_state:
    st.session_state.embedder = joblib.load("models/bert_embedder.pkl")

if 'encoders' not in st.session_state:
    st.session_state.encoders = joblib.load("models/label_encoders.pkl")

st.title("bug triage thingy")
st.write("put your bug title and desc here, then i'll try to guess the labels and stuff")

# user stuff
title = st.text_input("title of the bug", "Crash on login with valid credentials")
description = st.text_area("what happened?", "App crashes when user logs in using valid credentials.")

if st.button("go predict"):
    # clean input text
    user_df = pd.DataFrame([{
        "title": title,
        "description": description
    }])
    user_df = preprocess(user_df)
    input_text = user_df["text"].tolist()

    # get vector
    emb = st.session_state.embedder
    X = emb.encode(input_text)

    # predict time
    model = st.session_state.model
    pred = model.predict(X)

    # decode
    encoders = st.session_state.encoders
    cols = ['label', 'severity', 'priority', 'team']
    output = {}

    for i in range(len(cols)):
        col = cols[i]
        label = encoders[col].inverse_transform([pred[0][i]])[0]
        output[col] = label

    # show
    st.subheader("your prediction results")
    for k, v in output.items():
        st.write(f"{k} ➜ {v}")