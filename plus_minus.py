#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length = len(arr)
    pos = neg = zer = 0
    for i in arr:
        if i > 0:
            pos +=1
        elif i < 0:
            neg += 1
        else:
            zer += 1
    print(pos/length)
    print(neg/length)
    print(zer/length)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
