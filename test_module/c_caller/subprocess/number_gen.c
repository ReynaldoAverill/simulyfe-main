#include <stdlib.h>
#include <stdio.h>
// #include <time.h>
#include <unistd.h>

int main(){
    int i = 0;
    while(i<10){
        printf("i=%d\n",i);
        i++;
        sleep(1);
    }
}