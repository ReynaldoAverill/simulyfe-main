// C writer
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>

#define SHM_SIZE 1024

int main() {
    key_t key = ftok("shmfile", 65);
    int shmid = shmget(key, SHM_SIZE, 0666 | IPC_CREAT);
    char *data = (char *)shmat(shmid, (void *)0, 0);

    for (int i = 0; i < 10; i++) {
        sprintf(data, "Message %d from C program", i);
        sleep(1);
    }

    shmdt(data);
    return 0;
}