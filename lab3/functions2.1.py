def is_above_5_5(movie):
    return movie["imdb"] > 5.5

movie_example = {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
}

result = is_above_5_5(movie_example)
print(result) 
