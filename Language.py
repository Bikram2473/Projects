""" Language Detection """

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("language.csv")
print(data.head())
print("\n", data.isnull().sum())

df = data["language"].value_counts()
print("\n", df)

""" Language Detection Model """
x = np.array(data["Text"])
y = np.array(data["language"])

cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 45)

# Training the model
model = MultinomialNB()
model.fit(X_train, y_train)
model.score(X_test, y_test)

# Deploying the model
def languagedetection():
    user = st.text_area("Enter a text: ")
    if len(user) < 1:
        st.write(" ")
    else:
        sample = user
        data =cv.transform([sample]).toarray()
        a = model.predict(data)
        st.title(a)

languagedetection()