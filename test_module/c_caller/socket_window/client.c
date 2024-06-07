#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>

// Run code using this syntax
// gcc client.c -o client -lws2_32

#pragma comment(lib, "ws2_32.lib")  // Link with ws2_32.lib

#define PORT 65432

int main() {
    WSADATA wsa;
    SOCKET sock;
    struct sockaddr_in server;
    char *message;

    // Initialize Winsock
    printf("\nInitializing Winsock...");
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("Failed. Error Code: %d\n", WSAGetLastError());
        return 1;
    }
    printf("Initialized.\n");

    // Create a socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        printf("Could not create socket: %d\n", WSAGetLastError());
        WSACleanup();
        return 1;
    }
    printf("Socket created.\n");

    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    server.sin_family = AF_INET;
    server.sin_port = htons(PORT);

    // Connect to the server
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        printf("Connect error: %d\n", WSAGetLastError());
        closesocket(sock);
        WSACleanup();
        return 1;
    }
    printf("Connected to server.\n");

    // Send data to the server
    for (int i = 0; i < 10; i++) {
        message = "Hello from C client";
        if (send(sock, message, strlen(message), 0) < 0) {
            printf("Send failed: %d\n", WSAGetLastError());
            closesocket(sock);
            WSACleanup();
            return 1;
        }
        printf("Message sent.\n");
        Sleep(1000);  // Sleep for a second
    }

    // Clean up and close the socket
    closesocket(sock);
    WSACleanup();

    return 0;
}
