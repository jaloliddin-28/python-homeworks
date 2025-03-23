import requests
import random

my_key = 'e9a62ae84f316e7783a048c7bf0950dc'
base = "https://api.themoviedb.org/3"
def get_genres():
    url = f"{base}/genre/movie/list?api_key={my_key}&language=en-US"
    res = requests.get(url)
    if res.status_code == 200:
        return {genre['name']: genre['id'] for genre in res.json()['genres']}
    else:
        return {}

def get_movies(genre_id):
        url = f"{base}/discover/movie?api_key={my_key}&with_genres={genre_id}"
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()['results']
        else:
            return []
s = get_genres()
while True:
    d = int(input('What do you want? \n1. Get a recommended movie\n2. See the list of genres\n3. Quit the program\n'))
    if d == 1:
        print(s)
        genre_id = int(input("From the list above, choose your favourite genre and enter its ID: "))
        if genre_id in list(s.values()):
            list = get_movies(genre_id)
        else:
            print('Invalid id.')
            continue
        movie = random.choice(list)
        print(f"Recommended Movie: {movie['title']} ({movie['release_date'][:4]})\nOverview: {movie['overview']}")
    elif d == 2:
        print(s)
    elif d == 3:
        print("Stopping the program... ")
        break 
    else:
        print("Invalid number. Choose only 1-3.")