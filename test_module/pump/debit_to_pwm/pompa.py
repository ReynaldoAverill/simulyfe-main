import csv
import time
import RPi.GPIO as GPIO

# Define pin numbers
pwm_pin = 13
enable_pin1 = 19
enable_pin2 = 26

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(enable_pin1, GPIO.OUT)
GPIO.setup(enable_pin2, GPIO.OUT)

# Function to read data from CSV file
def read_csv_data(file_name):
    with open(file_name, 'r') as file:
        next(file)  # Skip the header row
        reader = csv.reader(file)
        data = list(reader)
    return data

# Function to find PWM value based on flow rate
def find_pwm(flow_rate, data):
    for row in data:
        if float(row[0]) == flow_rate:
            return int(row[1])
    return None

# Main program
def main():
    file_name = 'data_pompa.csv'
    data = read_csv_data(file_name)

    flow_rate = int(input("Masukkan flow rate yang diinginkan: "))

    pwm_value = find_pwm(flow_rate, data)

    if pwm_value is not None:
        # Set PWM pin
        pwm = GPIO.PWM(pwm_pin, 1000)
        pwm.start(pwm_value)

        # Activate the motor for 60 seconds
        GPIO.output(enable_pin1, GPIO.HIGH)
        GPIO.output(enable_pin2, GPIO.LOW)
        print("pwm yang digunakan adalah", pwm_value)

        time.sleep(60)

        # Stop PWM and cleanup GPIO
        pwm.stop()
        GPIO.cleanup()
    else:
        print("Flow rate tidak ditemukan dalam data.")

if __name__ == "__main__":
    main()
