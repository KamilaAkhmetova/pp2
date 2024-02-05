def average_imdb_score(movie_list):
    if not movie_list:
        return 0.0  

    total_score = sum(movie["imdb"] for movie in movie_list)
    average_score = total_score / len(movie_list)
    return average_score

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
]

result = average_imdb_score(movies)
print(result)
