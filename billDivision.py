#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
# k makanan yg ga dimakan sama anna
# b bill / 2

def bonAppetit(bill, k, b):
    # Write your code here
    res = 0
    anna_eat = bill
    anna_eat.pop(k)

    for i in anna_eat:
        res += i
    
    #split / 2
    result = res/2
    
    if b == result:
        print("Bon Appetit")
    else:
        result = b - result
        print(result)

if __name__ == '__main__':
    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = map(int, raw_input().rstrip().split())

    b = int(raw_input().strip())

    bonAppetit(bill, k, b)
