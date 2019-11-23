def quick_sort(A,l,r):
    if(l<r):
        p=partition(A,l,r)
        quick_sort(A,l,p-1)
        quick_sort(A,p+1,r)

def partition(A,l,r):
    i=l-1
    pivot=A[r]

    for j in range(l,r):
        if(A[j]<=pivot):
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def main():
    ar=input('Enter the elements that you wish to sort, separated by spaces:\n')
    A=ar.split(' ')
    for i in range(0,len(A)):
        temp=A[i]
        A[i]=int(temp)
    quick_sort(A,0,len(A)-1)
    print(A)
    
if(__name__=='__main__'):
    main()
