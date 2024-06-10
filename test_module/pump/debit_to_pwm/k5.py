import socket
import RPi.GPIO as GPIO
import time
import math
from threading import Thread, Event
import sys
import csv

HOST = '127.0.0.1'
PORT = 65432
PUMP_DURATION = 10

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define pin numbers
pwm_pin = 13
enable_pin1 = 19
enable_pin2 = 26

# Set up GPIO pins
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(enable_pin1, GPIO.OUT)
GPIO.setup(enable_pin2, GPIO.OUT)

# Create PWM instance
pwm = GPIO.PWM(pwm_pin, 1000)  # 1000 Hz frequency

# Start PWM with 0% duty cycle
pwm.start(0)
tabel_pwm = [0 for _ in range(25)]
j = 28
tanda = 29

# Shared variable to store the latest nilai_flow value
latest_nilai_flow = 0

# Event to control program termination
stop_event = Event()

# Fungsi untuk menulis ke file CSV
def write_to_csv():
    with open(f'data_pompa.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Flow', 'PWM'])  # Tulis header
        for i in range(24):
            writer.writerow([i+28, tabel_pwm[i]])

def handle_client(client_socket):
    global latest_nilai_flow
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        try:
            data = data.split("= ")[1]
            latest_nilai_flow = int(float(data))
            print("Received nilai_flow:", latest_nilai_flow)
            if latest_nilai_flow == 9999:
                stop_event.set()
                break
        except ValueError:
            print("Invalid data received")
    client_socket.close()

def control_pump():
    global latest_nilai_flow, j, tanda, stop_event
    try:
        while not stop_event.is_set():
            for i in range(40, 100):
                if stop_event.is_set():
                    break

                print("waktu adalah", i)
                GPIO.output(enable_pin1, GPIO.HIGH)
                GPIO.output(enable_pin2, GPIO.LOW)
                pwm.ChangeDutyCycle(i)

                nilai_flow = latest_nilai_flow

                if math.ceil(nilai_flow) == j and j < tanda < 55:
                    tabel_pwm[j-28] = i  # Store nilai_flow in tabel_pwm
                    j += 1
                    tanda += 1
                time.sleep(PUMP_DURATION)  # nyalakan selama 2 detik

                # Panggil fungsi untuk menulis ke CSV
                #write_to_csv()

            for i in range(0, 25):
                print("pwm untuk flow", 28+i, "adalah", tabel_pwm[i])
                print("\n")

            # Set flag to stop the program
            write_to_csv()
            GPIO.cleanup()
            sys.exit(0)
            stop_event.set()

    except KeyboardInterrupt:
        pass
    finally:
        # Clean up GPIO
        pwm.stop()
        GPIO.cleanup()

def run_socket_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Socket server listening on {HOST}:{PORT}")
    while not stop_event.is_set():
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = Thread(target=handle_client, args=(client_socket,))
        client_handler.daemon = True
        client_handler.start()

if __name__ == '__main__':
    # Start the control pump function in a separate thread
    control_thread = Thread(target=control_pump)
    control_thread.daemon = True
    control_thread.start()
    print("ini bagian 1 udah bisa")

    # Start the socket server in another thread
    socket_thread = Thread(target=run_socket_server)
    socket_thread.daemon = True
    socket_thread.start()
    print("ini bagian 2 udah bisa")

    # Wait for the control thread to finish
    control_thread.join()
    print("ini bagian 3 udah bisa")
    exit(1)

    # Stop the socket server by setting stop_event
    stop_event.set()
    socket_thread.join()  # Ensure socket thread also finishes
    print("ini bagian final udah bisa")

    # Clean up GPIO
    GPIO.cleanup()
