#!/bin/python3

import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    # Write your code here
    res = 0
    for i in range(len(ar)):
        for x in range(n):
            x += 1
            index = i + x
            if index < n:
                if (ar[i] + ar[index]) % k == 0:
                    res += 1
                
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
