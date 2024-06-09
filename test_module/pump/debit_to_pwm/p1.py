import csv
import time
import RPi.GPIO as GPIO  # Pastikan Anda sudah menginstal RPi.GPIO

# Inisialisasi pin PWM pada Raspberry Pi
pwm_pin = 18  # Ganti sesuai dengan pin yang Anda gunakan
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)

# Fungsi untuk membaca data dari file CSV
def baca_data_csv(nama_file):
    with open(nama_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

# Fungsi untuk mencari nilai PWM berdasarkan flow rate
def cari_pwm(flow_rate, data):
    for row in data:
        if int(row[0]) == flow_rate:
            return int(row[1])
    return None

# Main program
def main():
    # Baca data dari file CSV
    nama_file = 'data_pompa.csv'
    data = baca_data_csv(nama_file)

    # Minta input dari pengguna
    flow_rate = int(input("Masukkan flow rate yang diinginkan: "))

    # Cari nilai PWM dari data
    pwm_value = cari_pwm(flow_rate, data)

    if pwm_value is not None:
        # Atur PWM
        pwm = GPIO.PWM(pwm_pin, 1000)  # Frekuensi PWM 1000 Hz
        pwm.start(pwm_value)

        # Aktifkan pompa selama 60 detik
        time.sleep(60)

        # Matikan PWM dan reset GPIO
        pwm.stop()
        GPIO.cleanup()
    else:
        print("Flow rate tidak ditemukan dalam data.")

if __name__ == "__main__":
    main()
