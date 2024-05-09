import RPi.GPIO as GPIO
import time

# Definisikan pin yang akan digunakan
pinA = 9  # Kalo high, air masuk dari pipa kanan
pinB = 10  # Kalo high, air masuk dari pipa kiri
pin_pwm = 11

# Konfigurasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinA, GPIO.OUT)
GPIO.setup(pinB, GPIO.OUT)
GPIO.setup(pin_pwm, GPIO.OUT)

# Inisialisasi PWM
pwm = GPIO.PWM(pin_pwm, 1000)  # Frekuensi PWM 1000 Hz
pwm.start(0)  # Duty cycle awal 0%

try:
    while True:
        # Meminta input dari pengguna untuk durasi pompa (dalam detik)
        duration = int(input("Masukkan durasi pompa (detik): "))

        # Nyalakan pompa sesuai durasi yang dimasukkan
        GPIO.output(pinB, GPIO.HIGH)
        GPIO.output(pinA, GPIO.LOW)
        pwm.ChangeDutyCycle(100)  # Duty cycle 100%
        print("Pompa dinyalakan selama", duration, "detik.")
        time.sleep(duration)

        # Matikan pompa
        GPIO.output(pinB, GPIO.LOW)
        GPIO.output(pinA, GPIO.LOW)
        pwm.ChangeDutyCycle(0)  # Duty cycle 0%
        print("Pompa dimatikan.")

        # Menawarkan opsi untuk menyalakan kembali pompa atau keluar dari program
        option = input("Ingin menyalakan kembali pompa? (y/n): ")
        if option.lower() != 'y':
            break  # Keluar dari loop jika pengguna tidak ingin menyalakan kembali pompa

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
