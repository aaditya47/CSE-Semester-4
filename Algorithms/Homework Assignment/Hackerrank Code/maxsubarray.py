#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    max_val=arr[0]
    temp=arr[0]
    sum=0
    count=0
    for i in range(1,len(arr)):
        temp=max(arr[i],temp+arr[i])
        max_val=max(max_val,temp)
    for i in range(0,len(arr)):
        if(arr[i]>=0):
            sum+=arr[i]
        else:
            count+=1
    if(count==len(arr)):
        sum=max(arr)
    return max_val,sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
