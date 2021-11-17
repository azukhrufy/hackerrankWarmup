#!/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    # Write your code here
    
    minimum = 0
    maximum = 0
    count_min = 0
    count_max = 0
    init = True
    count = []
    for i in scores:
        if minimum == 0 and maximum == 0 and init == True:
            minimum = i
            maximum = i
            init = False
        elif i < minimum:
            minimum = i
            count_min += 1
        elif i > maximum:
            maximum = i
            count_max += 1
            
    count.append(count_max)
    count.append(count_min)
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
