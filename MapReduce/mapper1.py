#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if "," in line and line.count(",") >= 2:
        # Likely from movies.csv
        parts = line.split(",", 2)
        if len(parts) >= 2:
            movie_id = parts[0]
            title = parts[1]
            print("{}\tM:{}".format(movie_id, title))
    elif "\t" in line:
        # Likely from ratings average output
        parts = line.split("\t")
        if len(parts) == 2:
            movie_id, avg = parts
            print("{}\tR:{}".format(movie_id, avg))
