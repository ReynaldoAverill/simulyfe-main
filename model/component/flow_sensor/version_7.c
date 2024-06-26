/*
 * THIS FILE IS AUTOMATICALLY GENERATED
 *
 * Generator:     sensirion-driver-generator 0.32.0
 * Product:       sf06_lf
 * Model-Version: 1.1.0
 */
/*
 * Copyright (c) 2023, Sensirion AG
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * * Redistributions of source code must retain the above copyright notice, this
 *   list of conditions and the following disclaimer.
 *
 * * Redistributions in binary form must reproduce the above copyright notice,
 *   this list of conditions and the following disclaimer in the documentation
 *   and/or other materials provided with the distribution.
 *
 * * Neither the name of Sensirion AG nor the names of its
 *   contributors may be used to endorse or promote products derived from
 *   this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */
#include "sensirion_common.h"
#include "sensirion_i2c_hal.h"
#include "sf06_lf_i2c.h"
#include <stdio.h>  // printf
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 65432
#define SERVER_ADDR "127.0.0.1"

#define sensirion_hal_sleep_us sensirion_i2c_hal_sleep_usec
#define DELAY_FLOW_SENSOR 400000
#define N_REPETITION 200
#define N_AVERAGE 20
#define MAX_LEN 100

void print_byte_array(uint8_t* array, uint16_t len) {
    uint16_t i = 0;
    printf("0x");
    for (; i < len; i++) {
        printf("%02x", array[i]);
    }
}

void initialize_socket(int* sock){
    // Create a socket
    printf("\nInitializing Flow Sensor Client");
    if ((*sock = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Could not create socket");
        exit(1);
    }
    printf("Socket created.\n");
}

// Function to connect to server
void connect_to_server(int sock, const char* server_addr, int port) {
    struct sockaddr_in server;
    server.sin_addr.s_addr = inet_addr(server_addr);
    server.sin_family = AF_INET;
    server.sin_port = htons(port);

    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) == -1) {
        perror("Connect failed");
        close(sock);
        exit(1);
    }
    printf("Connected to server.\n");
}

// Function to send message to server
void send_message(int sock, char* message) {
    if (send(sock, message, strlen(message), 0) == -1) {
        perror("Send failed");
        close(sock);
        exit(1);
    }
    printf("Message sent: %s\n", message);
}

int main(void) {
    // Initalize connection to act as client
    int sock;
    char message[MAX_LEN];

    // Create a socket
    initialize_socket(&sock);

    // Connect to server
    connect_to_server(sock, SERVER_ADDR, PORT);

    // Initialize Flow Sensor
    int16_t error = NO_ERROR;
    sensirion_i2c_hal_init();
    sf06_lf_init(SLF3C_1300F_I2C_ADDR_08);

    sf06_lf_stop_continuous_measurement();
    sensirion_hal_sleep_us(100000);
    uint32_t product_identifier = 0;
    uint8_t serial_number[8] = {0};
    error =
        sf06_lf_read_product_identifier(&product_identifier, serial_number, 8);
    if (error != NO_ERROR) {
        char error_message[MAX_LEN];
        sprintf(error_message,"error executing read_product_identifier(): %i", error);
        printf("%s\n",error_message);
        send_message(sock,error_message);
        return error;
    }
    printf("product_identifier: %u ", product_identifier);
    printf("serial_number: ");
    print_byte_array(serial_number, 8);
    printf("\n");
    error = sf06_lf_start_h2o_continuous_measurement();
    if (error != NO_ERROR) {
        printf("error executing start_h2o_continuous_measurement(): %i\n",
               error);
        return error;
    }
    float a_flow = 0.0;
    float a_temperature = 0.0;
    uint16_t a_signaling_flags = 0u;
    uint16_t repetition = 0;

    float a_flow_20 = 0.0;

    int flag_tampil_flow = 0;	
	float total = 0;	  
    //int counter_total = 0;
  
    for (repetition = 0; repetition < N_REPETITION; repetition++) {
        flag_tampil_flow++;
        sensirion_hal_sleep_us(DELAY_FLOW_SENSOR);
        error = sf06_lf_read_measurement_data(500, &a_flow, &a_temperature, &a_signaling_flags);
        if (error != NO_ERROR) {
            printf("error executing read_measurement_data(): %i\n", error);
            continue;
        }
	    //printf("%.2f\n", a_flow);

        a_flow_20 += a_flow;
	    total += a_flow;

        if (flag_tampil_flow > N_AVERAGE){
            // printf("20 avg = %.2f\n", a_flow_20/21);
            sprintf(message,"Measured Flow (ml/min) = %.2f", a_flow_20/(N_AVERAGE+1));
            send_message(sock,message);
            flag_tampil_flow = 0;
            a_flow_20 = 0.0;
        }
        //printf("%.2f\n ", a_flow);
    }
    // sprintf(message,"Measured Flow is %.2f mL/min", total/repetition);
    // send_message(sock,message);
    error = sf06_lf_stop_continuous_measurement();
    if (error != NO_ERROR) {
        return error;
    }
    return NO_ERROR;
}
