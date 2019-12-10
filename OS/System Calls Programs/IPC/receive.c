/*
Shared Memory Program Template - Receiver Process
*/

#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 128
void main()
{
    key_t key=5678;
    // Connecting to the shared memory
    int shmid=shmget(key,MAXSIZE,0666);
    void *mem=shmat(shmid,NULL,0);

    // Now, mem is attached to the shared memory
    printf("Value entered in server: %d",mem);
    while(1)
    {

    }
}