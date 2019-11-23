def selection_sort(A):
    m=0
    for i in range(0,len(A)):
        m=i
        for j in range(i+1,len(A)):
            if(A[j]<A[m]):
                m=j
            A[i],A[m]=A[m],A[i]

def main():
    ar=input('Enter the elements that you wish to sort, separated by spaces:\n')
    A=ar.split(' ')
    for i in range(0,len(A)):
        temp=A[i]
        A[i]=int(temp)
    selection_sort(A)
    print(A)
    
if(__name__=='__main__'):
    main()
