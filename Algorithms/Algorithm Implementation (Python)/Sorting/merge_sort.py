import math

def merge_sort(A): 
    if(len(A)>1):
        mid=math.ceil(len(A)/2)
        left=A[:mid]
        right=A[mid:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        k=0
        
        while(i<len(left) and j<len(right)):
            if(left[i]<right[j]):
                A[k]=left[i]
                i+=1
            else:
                A[k]=right[j]
                j+=1
            k+=1

        while(i<len(left)):
            A[k]=left[i]
            i+=1
            k+=1

        while(j<len(right)):
            A[k]=right[i]
            j+=1
            k+=1        
                
def main():
    ar=input('Enter the elements that you wish to sort, separated by spaces:\n')
    A=ar.split(' ')
    for i in range(0,len(A)):
        temp=A[i]
        A[i]=int(temp)
    merge_sort(A)
    print(A)
    
if(__name__=='__main__'):
    main()
