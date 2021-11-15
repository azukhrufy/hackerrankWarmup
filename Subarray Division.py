import math
import os
import random
import re
import sys

def birthday(s, d, m):
    # Write your code here
    index = 0
    sum = 0
    match = 0
    
    for i in range(len(s)):
        sum = 0
        for x in range(m):
            if x+i < len(s):
                sum += s[x+i]
                print(x+i)
                
        if sum == d:
            match += 1
            
    return match

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
