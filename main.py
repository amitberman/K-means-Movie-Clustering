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

def count_all_actors_directors(df : pd.DataFrame) :
    actors_list = df['actors'].to_list()
    directors_list = df['director'].to_list()
    
    all_actors = []
    for movie_actors in actors_list:
        all_actors.extend(movie_actors)
    
    actors_counter = Counter(all_actors) 
    directors_counter = Counter(directors_list)
    
    return actors_counter.most_common(TOP_N_ACTORS) , directors_counter.most_common(TOP_M_DIRECTORS)
    
def ones_hot_vector(most_common , item_list):
    return [1 if item in item_list else 0 for item in most_common]


movies = []
for p in range(1,10):
    movies += best_movies_from_api(p)
df = pd.DataFrame(movies)[[
    "id",
    "genre_ids",
    "actors",
    "director"
]]

most_common_actors , most_common_directors = count_all_actors_directors(df[["actors" , "director"]])

print(most_common_actors ,most_common_directors)
