import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

API_KEY = "181722d95acd0d6f4074de4f524407ed"
TOP_N_ACTORS = 100
TOP_M_DIRECTORS = 20

def best_movies_from_api(indx:int): 
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={indx}"
    data_dic  = requests.get(url).json()
    data = data_dic['results']
    movies = []
 
    for movie in data :
        movie_id = movie["id"] 
        cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}"
        cast_data = requests.get(cast_url).json()['cast']
        crew_data = requests.get(cast_url).json()['crew']

        director = None
        actors = [m["id"] for m in cast_data if m.get("known_for_department") == "Acting"][:5]
        director = next((m["id"] for m in crew_data if m.get("job") == "Director"), None)

        
        movie['actors'] = actors
        movie['director'] = director

        movies.append(movie)
    return movies

def count_items(df : pd.DataFrame , col : str) :
    """the func calaculate all occurances of actors , directors , generes , etc ...
        it's designated to calc 1'hot vector later on
    Args:
        df (pd.DataFrame)
        col (str)

    Returns:
        Counter dict: {item id  : occurances}
    """
    all_items= []
    for value in df[col] :
        if isinstance(value , list):
            all_items.extend(value)
        else :
            all_items.append(value)
    
    
    return Counter(all_items)
    
def ones_hot_vector(most_common_items , movie_items):
    if isinstance(movie_items , list) :
        return [1 if item in movie_items else 0 for item in most_common_items]
    else :
        return [1 if item == movie_items else 0 for item in most_common_items]


movies = []
for p in range(1,10):
    movies += best_movies_from_api(p)
df = pd.DataFrame(movies)[[
    "id",
    "genre_ids",
    "actors",
    "director"
]]




