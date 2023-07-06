""" Netflix Movie Recommendation System """

import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("top10K-TMDB-movies.csv")
print(movies.head(10))
print("\n", movies.describe())
print("\n", movies.info())
print("\n", movies.isnull().sum())
print("\n", movies.columns)

movies = movies[['id', 'title', 'overview', 'genre']]
print("\n", movies)

movies['tags'] = movies['overview'] + movies['genre']
print("\n", movies)

new_data = movies.drop(columns = ['overview', 'genre'])
print("\n", new_data)

cv = CountVectorizer(max_features = 10000, stop_words = 'english')
print("\n", cv)

vector = cv.fit_transform(new_data['tags'].values.astype('U')).toarray()
print("\n", vector.shape)

similarity = cosine_similarity(vector)
print("\n", similarity)

df = new_data[new_data['title'] == "The Godfather"].index[0]
print("\n", df)
print("\n")

def recommend(movies):
    idx = new_data[new_data['title'] == movies].index[0]
    distance = sorted(list(enumerate(similarity[idx])), reverse = True, key = lambda vector:vector[1])
    for i in distance[0:5]:
        print(new_data.iloc[i[0]].title)

recommend("Iron Man")

pickle.dump(new_data, open('movies_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
p = pickle.load(open('movies_list.pkl', 'rb'))
print("\n", p)