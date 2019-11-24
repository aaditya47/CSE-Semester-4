def schedule(tasks):
    new_schedule=[]
    l=len(tasks)
    n=1
    new_schedule.append([])
    while(len(new_schedule)<l):
        minimum=0
        for i in range(1,len(tasks)):
            if(tasks[i][0]<tasks[minimum][0]):
                minimum=i
        t=tasks.pop(minimum)
        if(len(new_schedule[n-1])==0 or (t[1]<tasks[i][0] for i in range(0,len(tasks)))):
            new_schedule[n-1].append(t)
        else:
            n+=1
            new_schedule.append([])
            new_schedule[n-1].append(t)
    return new_schedule

def main():
    T=int(input('Enter the number of tasks: '))
    print("Enter the start and end time separated by space. Press enter to enter a new task:\n")
    tasks=[[] for i in range(0,T)]
    for i in range(0,T):
        temp=input().split(' ')
        tasks[i]=[int(x) for x in temp]
    new=schedule(tasks)
    print(new)
    
if(__name__=="__main__"):
    main()
