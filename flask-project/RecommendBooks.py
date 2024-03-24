from RecommendGenres import *
import numpy as np
import pandas as pd
import ast
import random

df = pd.read_csv('flask-project/cleaned_goodreads_data.csv') 

# Function to return array of name, description, index for the first time
books_array = []
def firstBookCall():
    random_indices = df.sample(n=12).index
    indices_array = random_indices.tolist()

    for i in indices_array:
        row = df.loc[i]
        books_array.append([row['Book'], row['Author'], row['Description'], row['Genres'], row['Avg_Rating'], i])

    return books_array

# Function to get a complete list of genres based on choices
allGenres = []
def getGenres(choices: list):
    for j in choices:
        if j < len(books_array):
            genresForBook = books_array[j][3].strip('[]').split(',')
            for genre in genresForBook:
                genre = genre.strip().strip('\'"')
                allGenres.append(genre)   

    return allGenres

# Function to generate recommendations based on array recieved from HTML
bookRecommendations = []
def getBookRecs(genresList: list):
    for i in range(0,len(genresList)):
        recommendation = recommend_genres(genresList[i])

        for rec in recommendation:
            bookRecommendations.extend(rec)

    if len(bookRecommendations) >= 12:
        return random.sample(bookRecommendations, 12)
    else:
        return bookRecommendations

print(firstBookCall())
choices = [0] #get from html
genres = getGenres(choices)
print(getBookRecs(genres))