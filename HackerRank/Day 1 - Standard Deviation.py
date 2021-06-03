#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    n = len(arr)
    res = 0
    avg = sum(arr)/n
    tmp = 0
    for i in arr:
        tmp += (i-avg)**2
    res = (tmp/n)**(1/2)
    print(round(res, 1))
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
