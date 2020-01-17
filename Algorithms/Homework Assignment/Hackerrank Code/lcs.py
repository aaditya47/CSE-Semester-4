#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    A=len(a)
    B=len(b)
    L = [[0]*(B+1) for i in range(A+1)]
    for i in range(0,A+1):
        for j in range(0,B+1):
            if (i==0 or j==0):
                L[i][j]==0
            elif (a[i-1]==b[j-1]):   
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i-1][j] , L[i][j-1])     

    target=L[A][B]
    lcs=[""]*(target+1)
    lcs[target]=""
    i=A
    j=B
    while i>0 and j>0:
        if a[i-1] == b[j-1]:
            lcs[target-1]=a[i-1]
            i-=1
            j-=1
            target-=1
        elif L[i-1][j] > L[i][j-1]:
             i-=1
        else:
            j-=1
    return lcs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
