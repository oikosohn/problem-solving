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

def quartiles(arr):
    # Write your code here
    # arr = [4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]
    n = len(arr)
            
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx] :
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
      
    mid = n//2
    lmid = mid//2
    umid = mid+mid//2  
    a,b,c = 0,0,0
    if n%2==0 : # even
        if mid%2 == 0:
            a = (arr[lmid-1]+arr[lmid])/2   
            b = (arr[mid-1]+arr[mid])/2
            c = (arr[umid-1]+arr[umid])/2
        else:
            a = arr[lmid]    
            b = (arr[mid-1]+arr[mid])/2
            c = arr[umid]
    else: # odd
        if mid%2 == 0:
            a = (arr[lmid-1]+arr[lmid])/2
            b = arr[mid]
            c = (arr[umid]+arr[umid+1])/2
        else:
            a = (arr[lmid])
            b = arr[mid]
            c = (arr[umid+1])
    
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
