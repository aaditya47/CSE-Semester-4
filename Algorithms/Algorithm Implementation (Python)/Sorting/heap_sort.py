def max_heapify(A,n,i):
    largest=i
    l=(2*i)+1
    r=(2*i)+2

    if(l<n and A[i]<A[l]):
        largest=l

    if(r<n and A[largest]<A[r]):
        largest=r

    if(largest!=i):
        A[i],A[largest]=A[largest],A[i]

        max_heapify(A,n,largest)

def heap_sort(A):
    n=len(A)
    
    for i in range(n,-1,-1):
        max_heapify(A,n,i)
    
    for i in range(n-1,0,-1):
        A[i],A[0]=A[0],A[i]
        max_heapify(A,i,0)

def main():
    ar=input('Enter the elements that you wish to sort, separated by spaces:\n')
    A=ar.split(' ')
    for i in range(0,len(A)):
        temp=A[i]
        A[i]=int(temp)
    heap_sort(A)
    print(A)
    
if(__name__=='__main__'):
    main()
