#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    standar_grade = []
    starter_grade = 40
    res = []
    
    for i in grades:
        val = int(i/5)
        grade = (val * 5) + 5
        if grade - i < 3:
            val = int(i/5)
            grade = (val * 5) + 5
            if grade < 40:
                grade = i
        else:
            grade = i
                
        res.append(grade)
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
