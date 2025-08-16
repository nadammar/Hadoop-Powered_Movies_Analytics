#!/usr/bin/env python3
import sys

# Read each line from standard input
for line in sys.stdin:
    fields = line.strip().split(",")
    
    # Skip the header
    if fields[0] == "userId":
        continue
    
    # Extract movieId and rating
    _, movie_id, rating, _ = fields
    
    print(f"{movie_id}\t{rating}")
