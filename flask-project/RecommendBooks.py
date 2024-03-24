from RecommendGenres import *
import numpy as np
import pandas as pd
import random

df = pd.read_csv('flask-project/FINAL_DATA.csv') 

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
    print("check GENRES")
    return allGenres

def getBookRecs(genresList: list):
    modifiedBookRecommendations = [] 
    for genre in genresList:
        recommendation = recommend_book_lists(genre)
        for rec in recommendation:
            modifiedBookRecommendations.append(rec)
    
    if len(modifiedBookRecommendations) < 12:
        needed = 12 - len(modifiedBookRecommendations)
        additional_books = df.sample(n=needed).reset_index()
        for i in range(needed):
            book = additional_books.iloc[i]
            modifiedBookRecommendations.append([book['Book'], book['Author'], book['Description'], book['Genres'], book['Avg_Rating'], book['index']])
    else:
        modifiedBookRecommendations = random.sample(modifiedBookRecommendations, 12)

    return [[book[0], book[1], book[2]] for book in modifiedBookRecommendations]

# Example usage
# firstBookCall()
# choices = [0,1,2]  # Example choices
# genres = getGenres(choices)
# print(getBookRecs(genres))