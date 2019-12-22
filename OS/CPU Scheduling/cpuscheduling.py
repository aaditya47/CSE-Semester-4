import os
def fcfs_wt(processes, n, burst_time, waiting_time):
    waiting_time[0]=0
    for i in range(1,n):
        waiting_time[i]=burst_time[i-1]+waiting_time[i-1]

def fcfs_tat(processes, n, burst_time, waiting_time, turn_around_time):
    for i in range(n):
        turn_around_time[i]=burst_time[i]+waiting_time[i]

def fcfs(processes, n, burst_time):
    waiting_time=[0]*n
    turn_around_time=[0]*n
    total_wt=0
    total_tat=0
    fcfs_wt(processes, n, burst_time,waiting_time)
    fcfs_tat(processes, n, burst_time, waiting_time, turn_around_time)
    for i in range(0,n):
        total_wt+=waiting_time[i]
    return (total_wt/n)