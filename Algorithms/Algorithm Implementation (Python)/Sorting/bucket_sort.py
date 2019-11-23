def bucket_sort(A):
    bucket=[]

    for i in range(len(A)):
        bucket.append([])

    for j in A:
        index_b=int(10*j)
        bucket[index_b].append(j)

    for i in range(len(A)):
        insertion_sort(bucket[i])

    k=0
    for i in range(len(A)):
        for j in range(len(bucket[i])):
            A[k]=bucket[i][j]
            k+=1
    return A
        

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
    bucket_sort(A)
    print(A)
    
if(__name__=='__main__'):
    main()
