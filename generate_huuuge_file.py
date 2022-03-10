""" This script creates a text file of bilion integers. """
import random

with open('huuuge.txt', 'w') as f:
    i = 1
    while i <= 1_000_000_000:
        f.write(f'{random.randint(0, 120)} ')
        if i % 25 == 0:
            f.write('\n')
        i += 1
