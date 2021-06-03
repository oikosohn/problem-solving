#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from statistics import median

def quartiles(arr):
    # Write your code here
    n = len(arr)
            
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx] :
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
      
    mid = n//2

    a,b,c = 0,0,0
    if n%2==0 : # even
        L = arr[:mid]
        U = arr[mid:]
    else:
        L = arr[:mid]
        U = arr[mid+1:]
    a = int(median(L))
    b = int(median(arr))
    c = int(median(U))   
    
    res = [a,b,c]
    return map(int, res)
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
