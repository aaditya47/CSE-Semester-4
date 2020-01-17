#include <iostream>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>

using namespace std;

int main()
{
    key_t key=ftok("sharedmem",65);
    int shmid=shmget(key,1024,0666|IPC_CREAT);
    char *mem=(char*) shmat(shmid,(void*)0,0); // To read strings. Type cast accordingly
    // write to the shared memory by assigning value to mem
    shmdt(mem);
}