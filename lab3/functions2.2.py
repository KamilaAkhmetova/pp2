def above_5_5_movies(movie_list):
    return [movie for movie in movie_list if movie["imdb"] > 5.5]

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
]

result = above_5_5_movies(movies)
print(result)

