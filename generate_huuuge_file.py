""" This script creates a text file of bilion integers. """
import random

with open('huuge.txt', 'w', encoding='utf-8') as f:
    i = 1
    while i <= 1_000_000:
        f.write(f"{random.randint(0, 121)} ")
        if i % 25 == 0:
            f.write('\n')
        i += 1
