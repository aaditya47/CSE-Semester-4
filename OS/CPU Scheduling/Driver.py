import cpuscheduling as sc
def main():
    n=int(input("Enter the number of processes to be scheduled: "))
    processes=[i for i in range(0,n)]
    burst_time=[0]*n
    for i in range(0,n):
        print("Enter burst time of process %d: "%(i+1),end='')
        burst_time[i]=int(input())
    print("FCFS Waiting Time: %.2f"%(sc.fcfs(processes,n,burst_time)))

if(__name__=="__main__"):
    main()