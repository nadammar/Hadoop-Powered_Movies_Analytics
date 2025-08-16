#!/usr/bin/env python3
import sys

current_movie = None
total_rating = 0.0
count = 0

for line in sys.stdin:
    movie_id, rating = line.strip().split("\t")
    if current_movie == movie_id:
        total_rating += float(rating)
        count += 1
    else:
        if current_movie:
            average = total_rating / count
            print(f"{current_movie}\t{average:.2f}")
        current_movie = movie_id
        total_rating = float(rating)
        count = 1

if current_movie == movie_id:
    average = total_rating / count
    print(f"{current_movie}\t{average:.2f}")
