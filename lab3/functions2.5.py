def average_imdb_score_by_category(movie_list, category):
    category_movies = [movie for movie in movie_list if movie["category"] == category]

    if not category_movies:
        return 0.0  

    total_score = sum(movie["imdb"] for movie in category_movies)
    average_score = total_score / len(category_movies)
    return average_score

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
]

category_name = "Romance"
result = average_imdb_score_by_category(movies, category_name)
print(result)
