#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    if s[-2] == "P":
        get_pm = s.split("PM")
        time = get_pm[0].split(":")
        
        if int(time[0]) < 12:
            new_time_int = int(time[0]) + 12
            new_time = str(new_time_int) + ":" + time[1] + ":" + time[2]
            return new_time
        else:
            return get_pm[0]
    if s[-2] == "A":
        get_am = s.split("AM")
        time = get_am[0].split(":")
        
        if int(time[0]) < 12:
            return get_am[0]
        else:
            new_time_int = int(time[0]) - 12
            new_time = "0" + str(new_time_int) + ":" + time[1] + ":" + time[2]
            return new_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
