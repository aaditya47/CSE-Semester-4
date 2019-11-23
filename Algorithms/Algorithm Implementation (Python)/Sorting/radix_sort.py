import math
def counting_sort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]
    

def radix_sort(A):
    max1=max(A)
    exp=1
    while(max1/exp > 0):
        counting_sort(A,exp)
        exp*=10

def main():
    ar=input('Enter the elements that you wish to sort, separated by spaces:\n')
    A=ar.split(' ')
    for i in range(0,len(A)):
        temp=A[i]
        A[i]=int(temp)
    radix_sort(A)
    print(A)
    
if(__name__=='__main__'):
    main()
