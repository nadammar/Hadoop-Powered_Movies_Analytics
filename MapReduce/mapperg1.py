#!/usr/bin/env python3
import sys

# Load the movies data into a dictionary
movies = {}
with open('movies.csv', 'r', encoding='utf-8') as f:
    next(f)  # Skip header
    for line in f:
        fields = line.strip().split(',', 2)
        movie_id, title, genres = fields[0], fields[1], fields[2]
        movies[movie_id] = (title, genres)

# Process ratings input
for line in sys.stdin:
    try:
        fields = line.strip().split(',')
        if len(fields) < 4:
            continue
        movie_id, rating = fields[1], float(fields[2])
        
        if movie_id in movies:
            title, genres = movies[movie_id]
            for genre in genres.split('|'):
                # Output format: genre \t movie_name \t rating
                print("{}\t{}\t{}".format(genre, title, rating))
    except Exception as e:
        continue
