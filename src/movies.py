import pandas as pd
import numpy as np

movies = pd.read_csv('./data/movietweetings/movies.dat', delimiter='::',
                     engine='python', header=None, names=['Movie ID', 'Movie Title', 'Genre'])

print(movies.head())


users = pd.read_csv('./data/movietweetings/users.dat', delimiter='::',
                    engine='python', header=None, names=['User ID', 'Twitter ID'])
ratings = pd.read_csv('./data/movietweetings/ratings.dat', delimiter='::', engine='python',
                      header=None, names=['User ID', 'Movie ID', 'Rating', 'Rating Timestamp'])

print(users.head())
print(ratings.head())

movies.loc['Genre']
