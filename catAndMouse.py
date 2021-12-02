#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the catAndMouse function below.
#
def catAndMouse(x, y, z):
    #
    # Write your code here.
    #
    
    # get the distance 
    cat_a = z - x
    cat_b = z - y
    
    if cat_a < 0 :
        cat_a = cat_a * -1
    if cat_b < 0:
        cat_b = cat_b * -1
        
    if cat_a == cat_b:
        return ("Mouse C")
    elif cat_a > cat_b:
        return ("Cat B")
    else:
        return ("Cat A")


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        xyz = raw_input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        f.write(result + '\n')

    f.close()