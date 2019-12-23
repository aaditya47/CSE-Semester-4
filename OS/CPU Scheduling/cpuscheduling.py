import os

class Process:
    def __init__(self,pid,at,bt,pr):
        self.id=pid
        self.arrival_time=at
        self.burst_time=bt
        self.priority=pr

def fcfs_wt(processes, n, burst_time, waiting_time):
    waiting_time[0]=0
    for i in range(1,n):
        waiting_time[i]=processes[i-1].burst_time+waiting_time[i-1] # Process i's waiting time = burst time of process i-1 + waiting time of process i-1 (fcfs property)

def fcfs_tat(processes, n, burst_time, waiting_time, turn_around_time):
    for i in range(n):
        turn_around_time[i]=processes[i].burst_time+waiting_time[i] # TAT = WT + BT

def fcfs(processes, n):
    waiting_time=[0]*n
    turn_around_time=[0]*n
    total_wt=0
    total_tat=0
    fcfs_wt(processes, n, burst_time,waiting_time)
    fcfs_tat(processes, n, burst_time, waiting_time, turn_around_time)
    for i in range(0,n):
        total_wt+=waiting_time[i]
    return (total_wt/n)

'''
Formulas:
TAT = Completion time - Arrival time
WT = TAT - BT
'''