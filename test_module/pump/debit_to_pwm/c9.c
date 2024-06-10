#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <math.h>

// Function to send nilai_flow to the server
void send_nilai_flow(int nilai_flow) {
    int sock;
    struct sockaddr_in server;
    char message[50];

    // Create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        printf("Could not create socket");
        return;
    }
    puts("Socket created");

    server.sin_addr.s_addr = inet_addr("127.0.0.1"); // Use the server's IP address
    server.sin_family = AF_INET;
    server.sin_port = htons(5000);

    // Connect to remote server
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        perror("connect failed. Error");
        return;
    }

    puts("Connected");

    // Prepare the message
    snprintf(message, sizeof(message), "%d", nilai_flow);

    // Send the message
    if (send(sock, message, strlen(message), 0) < 0) {
        puts("Send failed");
        return;
    }

    puts("Data Sent\n");

    // Close the socket
    close(sock);
}

// Function to continuously update nilai_flow every two seconds
void *update_nilai_flow(void *arg) {
    float nilai_flow;
    int random;
    int flow_sementara;

    while (1) {
        for (int indeks = 28; indeks < 54; indeks++) {
            // Generate or fetch nilai_flow here (e.g., from sensors)
            flow_sementara = indeks;
            nilai_flow = flow_sementara;
            random = rand() % 6;
            random += 2;            
            sleep(random);
            send_nilai_flow((int)ceil(nilai_flow));
        }
        send_nilai_flow(9999);
        break;
    }

    return NULL;
}

int main() {
    pthread_t tid;
    pthread_create(&tid, NULL, update_nilai_flow, NULL);
    pthread_join(tid, NULL);

    return 0;
}
