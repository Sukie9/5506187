#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # Split the name into individual words
    words = s.split()

    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words back into a single string
    capitalized_name = ' '.join(capitalized_words)

    return capitalized_name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') if 'OUTPUT_PATH' in os.environ else sys.stdout

    s = input().strip()

    result = solve(s)

    fptr.write(result + '\n')

    if fptr != sys.stdout:
        fptr.close()
