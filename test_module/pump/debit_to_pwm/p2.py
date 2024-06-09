import csv
import time
import RPi.GPIO as GPIO

pwm_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)

def baca_data_csv(nama_file):
    with open(nama_file, 'r') as file:
        next(file)  # Skip the header row
        reader = csv.reader(file)
        data = list(reader)
    return data

def cari_pwm(flow_rate, data):
    for row in data:
        if float(row[0]) == flow_rate:
            return int(row[1])
    return None

def main():
    nama_file = 'data_pompa.csv'
    data = baca_data_csv(nama_file)

    flow_rate = int(input("Masukkan flow rate yang diinginkan: "))

    pwm_value = cari_pwm(flow_rate, data)

    if pwm_value is not None:
        pwm = GPIO.PWM(pwm_pin, 1000)
        pwm.start(pwm_value)

        time.sleep(60)

        pwm.stop()
        GPIO.cleanup()
    else:
        print("Flow rate tidak ditemukan dalam data.")

if __name__ == "__main__":
    main()
