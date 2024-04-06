#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'countPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY pieces
#  2. INTEGER k
#

pieces=[15, 7, 15, 19, 81, 23, 41] 
k=10

def countPairs(pieces, k):
    # Write your code here
    n=len(pieces)
    rows=n
    cols=n
    matrix=[[0 for _ in range(cols)] for _ in range(rows)]
    print(matrix)


#if __name__ == '__main__':
 #   fptr = open(os.environ['OUTPUT_PATH'], 'w')

  #  first_multiple_input = input().rstrip().split()

   # k = int(first_multiple_input[0])

    #n = int(first_multiple_input[1])

    #pieces = []

    #for _ in range(n):
     #   pieces_item = int(input().strip())
      #  pieces.append(pieces_item)

    #result = countPairs(pieces, k)

    #fptr.write(str(result) + '\n')

    #fptr.close()//
