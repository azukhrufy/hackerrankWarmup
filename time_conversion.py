#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    
    
    if s[8] == "P":
        get_pm = s.split("PM")
        if get_pm[1] == "":
            time = get_pm[0].split(":")
            
            if int(time[0]) < 12:
                new_time_int = int(time[0]) + 12
                new_time = str(new_time_int) + ":" + time[1] + ":" + time[2]
                return new_time
            else:
                return get_pm[0]
    if s[8] == "A":
        get_am = s.split("AM")
        if get_am[1] == "":
            time = get_am[0].split(":")
            
            if int(time[0]) < 12:
                return get_am[0]
            else:
                new_time_int = int(time[0]) - 12
                new_time = "0" + str(new_time_int) + ":" + time[1] + ":" + time[2]
                return new_time
    
    
    # return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
