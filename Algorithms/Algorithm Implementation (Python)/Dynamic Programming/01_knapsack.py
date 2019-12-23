def rec_knapsack(W,wt,val,k):
    if(k==0 or W==0):
        return 0
    if(wt[k-1]>W):
        return rec_knapsack(W,wt,val,k-1)
    else:
        return max(val[k-1]+rec_knapsack(W-wt[n-1],wt,val,k-1),rec_knapsack(W,wt,val,k-1))

'''
Recursive implementation of the 0-1 Knapsack Problem. 
Complexity: O(2^n), making it less ideal for larger values of n
'''

def botton_up_knapsack(W,wt,val,k):
    K=[[0 for i in range(W+1)] for j in range(k+1)]
    for i in range(0,k+1):
        for w in range(0,W+1):
            if(i==0 or w==0):
                K[i][w]=0
            elif(wt[i-1]<=w):
                K[i][w]=max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]
    return K[k][w]

'''
Bottom up implementation of the 0-1 Knapsack Problem.
Complexity: O(nW), signifying that the time complexity of this algorithm depends on the weight of the knapsack too. 
Making this algorithm pseudopolynomial
'''