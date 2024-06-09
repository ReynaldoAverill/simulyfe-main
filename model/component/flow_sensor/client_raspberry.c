#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 65432
#define SERVER_ADDR "127.0.0.1"
#define MAX_LEN 100

int main() {
    int sock;
    struct sockaddr_in server;
    char message[MAX_LEN];
    // char buffer[1024];
    // int recv_size;

    // Create a socket
    printf("\nInitializing Flow Sensor Client");
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Could not create socket");
        exit(1);
    }
    printf("Socket created.\n");

    server.sin_addr.s_addr = inet_addr(SERVER_ADDR);
    server.sin_family = AF_INET;
    server.sin_port = htons(PORT);

    // Connect to server
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) == -1) {
        perror("Connect failed");
        close(sock);
        exit(1);
    }
    printf("Connected to server.\n");

    // Send message to server
    for(int i = 0; i < 100; i++){
        sprintf(message,"Debit = %d",i);
        // message = "Hello from C client";
        if (send(sock, message, strlen(message), 0) == -1) {
            perror("Send failed");
            close(sock);
            exit(1);
        }
        printf("Message sent.\n");
        sleep(1);
    }

    // Receive response from server
    // if ((recv_size = recv(sock, buffer, 1024, 0)) == -1) {
    //     perror("Receive failed");
    //     close(sock);
    //     exit(1);
    // }
    // buffer[recv_size] = '\0';
    // printf("Response from server: %s\n", buffer);

    // Close socket
    close(sock);

    return 0;
}
