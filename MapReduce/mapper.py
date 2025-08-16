#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split(",")
    if len(parts) != 4 or parts[0] == "userId":
        continue
    movie_id = parts[1]
    rating = parts[2]
    print(f"{movie_id}\t{rating}")
