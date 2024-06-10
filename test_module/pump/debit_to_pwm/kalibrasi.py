from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import time
import math
from threading import Thread, Event
import sys
import csv  # Tambahkan library CSV

app = Flask(__name__)

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
tabel_pwm = [0 for _ in range(24)]
j = 28
tanda = 29

# Shared variable to store the latest nilai_flow value
latest_nilai_flow = 0

# Event to control program termination
stop_event = Event()

# Fungsi untuk menulis ke file CSV
def write_to_csv():
    with open('data_pompa.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Flow', 'PWM'])  # Tulis header
        for i in range(24):
            writer.writerow([i+28, tabel_pwm[i]])

@app.route('/nilai_flow', methods=['POST'])
def receive_nilai_flow():
    global latest_nilai_flow
    data = request.json

    if 'nilai_flow' in data:
        latest_nilai_flow: str = data['nilai_flow']
        latest_nilai_flow = int(float(latest_nilai_flow.split("= ")[1]))
        print("Received nilai_flow:", latest_nilai_flow)  # Display the received data
        if latest_nilai_flow == 9999:
            stop_event.set()

        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

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

                if math.ceil(nilai_flow) == j and j < tanda < 53:
                    tabel_pwm[j-28] = i  # Store nilai_flow in tabel_pwm
                    j += 1
                    tanda += 1
                time.sleep(5)  # nyalakan selama 2 detik

                # Panggil fungsi untuk menulis ke CSV
                write_to_csv()

            for i in range(0, 24):
                print("pwm untuk flow", 28+i, "adalah", tabel_pwm[i])
                print("\n")

            # Set flag to stop the program
            GPIO.cleanup()
            sys.exit(0)
            stop_event.set()

    except KeyboardInterrupt:
        pass
    finally:
        # Clean up GPIO
        pwm.stop()
        GPIO.cleanup()

def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    # Start the control pump function in a separate thread
    control_thread = Thread(target=control_pump)
    control_thread.daemon = True
    control_thread.start()
    print("ini bagian 1 udah bisa")

    # Start the Flask server in another thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    print("ini bagian 2 udah bisa")
    #flask_thread.join()  # Ensure Flask thread also finishes

    # Wait for the control thread to finish
    control_thread.join()
    exit(1)
    print("ini bagian 3 udah bisa")

    # Stop the Flask server by setting stop_event
    stop_event.set()
    flask_thread.join()  # Ensure Flask thread also finishes
    print("ini bagian final udah bisa")
