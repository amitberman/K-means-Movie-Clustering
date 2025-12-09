import requests

API_KEY = "181722d95acd0d6f4074de4f524407ed"

url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={1}"
data_dic  = requests.get(url).json()
total_res = data_dic['total_results']
data = data_dic['results']
print(data[0].keys())
