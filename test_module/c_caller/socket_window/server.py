import socket
import threading
import time

from subprocess import Popen, PIPE, STDOUT

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def handle_client(conn: socket.socket, addr):
    # Started when server receive data from client/when client is active
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")

def print_random():
    while True:
        print("Hi from random function")
        time.sleep(5)

def start_c():
    executable  = ['gcc','-o','client','client.c','-lws2_32']
    command     = [".\client"]
    # perintah = "./coba"

    proc1 = Popen(executable)
    proc1.wait()
    print("exe file created")
    proc = Popen(command, stdout = PIPE, stderr = PIPE,text=True,universal_newlines=True)
    print("exe file opened")

def main():
    threading.Thread(target= print_random).start()
    print("Started thread for print random") 
    start_c()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
            print(f"Started thread for {addr}")

if __name__ == "__main__":
    main()
