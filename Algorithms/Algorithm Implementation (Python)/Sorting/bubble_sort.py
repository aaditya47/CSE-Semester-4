def bubble_sort(A):
    for i in range(len(A)-1,0,-1):
        for j in range(i):
            if(A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]

def main():
    ar=input('Enter the elements that you wish to sort, separated by spaces:\n')
    A=ar.split(' ')
    for i in range(0,len(A)):
        temp=A[i]
        A[i]=int(temp)
    bubble_sort(A)
    print(A)
    
if(__name__=='__main__'):
    main()
