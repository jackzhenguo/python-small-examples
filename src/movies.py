import pandas as pd
import numpy as np

movies = pd.read_csv('./data/movietweetings/movies.dat', delimiter='::',
                     engine='python', header=None, names=['Movie ID', 'Movie Title', 'Genre'])
users = pd.read_csv('./data/movietweetings/users.dat', delimiter='::',
                    engine='python', header=None, names=['User ID', 'Twitter ID'])
ratings = pd.read_csv('./data/movietweetings/ratings.dat', delimiter='::', engine='python',
                      header=None, names=['User ID', 'Movie ID', 'Rating', 'Rating Timestamp'])

print(movies.head(10))
mask = movies.Genre.str.contains('comedy', case=False, na=False)
print(mask.head(10))
comedy = movies[mask]
comedy_ids = comedy['Movie ID']
print(comedy_ids.head(10))

combine = ratings.join(comedy, on='Movie ID', rsuffix='right')
print(combine.head(50))
result = combine[combine['Movie IDright'] != np.NaN]
print(result)
