#!/usr/bin/env python3
import sys
from collections import defaultdict

# Load the movie genres from the file
movies = {}
with open('/data/movies.csv', 'r') as file:
    next(file)  # skip header
    for line in file:
        movie_id, title, genres = line.strip().split(",", 2)
        movies[movie_id] = (title, genres.split("|"))

# Initialize containers
movie_ratings = defaultdict(list)

# Read input from mapper
for line in sys.stdin:
    movie_id, rating = line.strip().split("\t")
    if movie_id in movies:
        movie_ratings[movie_id].append(float(rating))

# Calculate average and group by genre
genre_top_movies = defaultdict(list)

for movie_id, ratings in movie_ratings.items():
    title, genres = movies[movie_id]
    average = sum(ratings) / len(ratings)
    for genre in genres:
        genre_top_movies[genre].append((average, title))

# Output top 10 for each genre
for genre, movies in genre_top_movies.items():
    top_movies = sorted(movies, reverse=True)[:10]
    for avg, title in top_movies:
        print(f"{genre}\t{title}\t{avg:.2f}")
