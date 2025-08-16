#!/usr/bin/env python3
import sys
from collections import defaultdict

# Initialize storage
genre_movies = defaultdict(lambda: defaultdict(list))

# Read input from Mapper
for line in sys.stdin:
    try:
        genre, title, rating = line.strip().split('\t')
        rating = float(rating)
        genre_movies[genre][title].append(rating)
    except ValueError:
        continue

# Process and sort movies by genre
for genre, movies in genre_movies.items():
    # Calculate the average rating for each movie
    sorted_movies = sorted(
        [(title, sum(ratings) / len(ratings)) for title, ratings in movies.items()],
        key=lambda x: -x[1]
    )
    
    # Output the top 20 movies in each genre
    for title, average in sorted_movies[:20]:
        print("{}\t{}\t{:.2f}".format(genre, title, average))
