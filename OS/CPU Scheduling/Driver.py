import cpuscheduling as sc

class Process:
    def __init__(self,pid,at,bt,pr):
        self.id=pid
        self.arrival_time=at
        self.burst_time=bt
        self.priority=pr

def main():
    print("Enter:\n1 for FCFS scheduling\n2 for SJF\n3 for Priority scheduling")
    opt=int(input())
    if(opt==1):
        n=int(input("Enter the number of processes to be scheduled: "))
        processes=[None]*n
        for i in range(0,n):
            processes[i]=sc.Process(i,0,0,0)
        for i in range(0,n):
            print("Enter burst time of process %d: "%(i+1),end='')
            processes[i].burst_time=int(input())
            print("FCFS Waiting Time: %.2f"%(sc.fcfs(processes,n)))
    '''
    elif(opt==2):
        # To fill in
    elif(opt==3):
        # To fill in
    '''

if(__name__=="__main__"):
    main()
