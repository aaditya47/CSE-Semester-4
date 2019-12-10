/*
Shared Memory Program Template - Sender Process
*/

#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 128

int main()
{
    int shmid;
    key_t key=5678;
    void *mem; // Memory to be sent
    char *s;
    shmid=shmget(key,MAXSIZE,IPC_CREAT | 0666); 
/*  Creates a shared memory, and returns the ID.
    Parameters for shmget: 
    key - unique identifier for the shared memory
    size - size of the shared memory
    permissions - chmod style permissions selector  */
    mem=shmat(shmid,NULL,0);
/*  Attaches the pointer onto the shared memory.
    Parameters for shmat:
    shmid - identifier returned from shmget
    shmaddr - desired address of shared memory
    shmflg - specifies set of flags

    mem can now be used to store whatever that needs to be stored in shared memory  */

    printf("Enter a number to store on the shared memory: ");
    scanf("%d",&mem);
}