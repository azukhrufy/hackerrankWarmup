#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    index = 0
    res = result = final = 0
    primary = []
    secondary = []
    length = len(arr)
    for i in range(length):
        primary.append(index)
        secondary.append((length - 1) - index)
        index += 1
    
    for i in secondary:
        print(i)
    index = 0
    for i in primary:
        res += arr[i][i]
    
    for y in secondary:
        result += arr[index][y]
        index += 1
    
    final = res - result
    if final < 0:
        return final * -1
    else:
        return final

        
        
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
