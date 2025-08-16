#!/usr/bin/env python3
import sys

current_movie = None
title = None
avg = None

for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t", 1)
    if len(parts) != 2:
        continue

    movie_id, value = parts

    if current_movie != movie_id:
        if title and avg:
            print("{:.2f}\t{}".format(float(avg), title))
        current_movie = movie_id
        title = None
        avg = None

    if value.startswith("M:"):
        title = value[2:]
    elif value.startswith("R:"):
        avg = value[2:]

# Output last movie
if title and avg:
    print("{:.2f}\t{}".format(float(avg), title))
