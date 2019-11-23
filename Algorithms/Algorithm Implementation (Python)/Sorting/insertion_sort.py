def insertion_sort(A):
    for i in range(1,len(A)):
        key=A[i]
        j=i-1
        while(j>=0 and key<A[j]):
            A[j+1]=A[j]
            j-=1
        A[j+1]=key

def main():
    ar=input('Enter the elements that you wish to sort, separated by spaces:\n')
    A=ar.split(' ')
    for i in range(0,len(A)):
        temp=A[i]
        A[i]=int(temp)
    insertion_sort(A)
    print(A)
    
if(__name__=='__main__'):
    main()
