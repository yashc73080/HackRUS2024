from RecommendGenres import *
import numpy as np
import pandas as pd

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
        genresForBook = books_array[j][3]
        for genre in genresForBook:
            print(genre)
            # allGenres.append(genre)
    
    print(genresForBook)

firstBookCall()
getGenres([0])


# Function to generate recommendations based on array recieved from HTML