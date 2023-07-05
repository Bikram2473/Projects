""" Spam Detection System """

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("SpamDetection.csv", encoding = 'latin-1')
data = data[["class", "message"]]

x = np.array(data["message"])
y = np.array(data["class"])

cv = CountVectorizer()
X = cv.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)

clf = MultinomialNB()
clf.fit(x_train, y_train)

st.title("Spam Detection System")
def spamdetection():
    user = st.text_area("Enter any message or email: ")
    if len(user) < 1:
        st.write(" ")
    else:
        sample = user
        data = cv.transform([sample]).toarray()
        a = clf.predict(data)
        st.title(a)

spamdetection()