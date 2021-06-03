#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median
#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = []
    for i in range(len(values)):
        arr += [values[i]]*freqs[i]
        
    n = len(arr)
    mid = n//2
    
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]   
        

    if n%2 == 0:
        L = arr[:mid]
        U = arr[mid:]
    else:
        L = arr[:mid]
        U = arr[mid+1:]

    iqr = float(median(U)-median(L))
    print(round(iqr, 1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
