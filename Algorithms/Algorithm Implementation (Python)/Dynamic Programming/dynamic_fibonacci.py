'''
Program that determines n'th Fibonacci number using the bottum-up memoization approach
'''
def fib(n) -> int:
    memo=[0]*n
    memo[0]=1
    memo[1]=1
    for i in range(2,n):
        memo[i]=memo[i-1]+memo[i-2]
    return memo[n-1]

def main():
    n=int(input("Enter the value of n: "))
    fib_n=fib(n)
    print("The ",n,"th fibonacci number is ",fib_n)

if(__name__=="__main__"):
    main()

'''
Analysis:
- Normal recursive fibonacci sequence takes O(2^n) time as every single recursive call needs to be evaluated
- Memoization speeds up this computation by storing intermediate values in an array, allowing it to run in O(n) time
'''