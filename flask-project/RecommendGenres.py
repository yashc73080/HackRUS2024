
## Data Processing and Cleaning
import numpy as np
import pandas as pd

df = pd.read_csv('flask-project/goodreads_data.csv')

df.drop('uselessNumbers', axis=1, inplace=True)
df.drop('Num_Ratings', axis=1, inplace=True)
df.drop('URL', axis=1, inplace=True)

df = df[df['Genres'].astype(str) != '[]']
df = df.reset_index(drop=True)


# Making the Model

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Text Vectorization

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Genres']) 

# Training Model

model = NearestNeighbors(n_neighbors=5, algorithm='brute')
model.fit(X)

# Predictions

def recommend_genres(genre):
    query = vectorizer.transform([genre])
    distances, indices = model.kneighbors(query)
    # return df['Genres'].iloc[indices[0]]
    return df[['Book', 'Author', 'Description', 'Genres', 'Avg_Rating']].iloc[indices[0]].values.tolist()

# Test

# print(recommend_genres('Dystopia'))