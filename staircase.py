#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    value = "#"
    space = " "
    index = []
    i = 1
    for x in range(n):
        index.append(n-i)
        i += 1
    z = 1
    for y in index:
        if y != 0:
            print("%s %s" % (space * (y-1),value * z))
        else:
            print("%s" % (value * z))
        z += 1
        
            
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
