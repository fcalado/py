# Version 1.0"
# Split big files in small parts by number of rows 

import pandas as pd
import numpy as np
import os

def split_file(bigFile, rows):
    with open(bigFile, 'r') as infile:
        lines = infile.readlines()

    numFiles = len(lines) // rows

    for i in range(numFiles):
        start = i * rows
        end = (i + 1) * rows
        pt = i + 1
        smallFile = f'{bigFile[:-4]}_pt_{pt:02}.{bigFile[-3:]}'

        with open(smallFile, 'w') as outfile:
            outfile.writelines(lines[start:end])

# file = 'data\customers.csv'
# rows = 500000
# split_file(file,rows)