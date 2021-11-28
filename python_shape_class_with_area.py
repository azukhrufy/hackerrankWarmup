#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self,a,b):
        if a != False:
            self.a = a
        else:
            self.a = 1
        if b != False:
            self.b = b
        else:
            self.b = 1
    
    def area(self):
        return self.a * self.b
    

class Circle:
    def __init__(self,r):
        self.r = r
        
    def area(self):
        return math.pi * (self.r * self.r)
    

if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
