import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

API_KEY = "181722d95acd0d6f4074de4f524407ed"
def best_movies_from_api(indx:int): 
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={indx}"
    data_dic  = requests.get(url).json()
    data = data_dic['results']

    return [movie for movie in data]


movies = []
for p in range(1,10):
    movies += best_movies_from_api(p)
print(len(movies))
df = pd.DataFrame(movies)[[
    "id",
    "title",
    "overview",
    "popularity",
    "vote_average",
    "genre_ids"
]]
print(df.loc[df.index[-1] , "overview"])

