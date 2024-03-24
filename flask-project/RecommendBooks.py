from RecommendGenres import *
import numpy as np
import pandas as pd

df = pd.read_csv('flask-project/cleaned_goodreads_data.csv') 


# Function to return array of name, description, index for the first time

def firstBookCalls():
    random_indices = df.sample(n=12).index
    indices_array = random_indices.tolist()

    books_array = []
    for i in indices_array:
        row = df.loc[i]
        books_array.append([row['Book'], row['Author'], row['Description'], row['Avg_Rating'], i])

    return books_array

