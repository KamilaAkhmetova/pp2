def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
]

category_name = "Romance"
result = movies_by_category(movies, category_name)
print(result)
