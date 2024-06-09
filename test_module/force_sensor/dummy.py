import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711

hx = HX711(5, 6)

def printRawBytes(rawBytes):
    print(f"[RAW BYTES] {rawBytes}")

def printLong(rawBytes):
    print(f"[LONG] {hx.rawBytesToLong(rawBytes)}")

def printLongWithOffset(rawBytes):
    print(f"[LONG WITH OFFSET] {hx.rawBytesToLongWithOffset(rawBytes)}")

def printWeight(rawBytes):
    print(f"[WEIGHT] {hx.rawBytesToWeight(rawBytes)} gr")

def getRawBytesAndPrintAll():
    rawBytes = hx.getRawBytes()
    longValue = hx.rawBytesToLong(rawBytes)
    longWithOffsetValue = hx.rawBytesToLongWithOffset(rawBytes)
    weightValue = hx.rawBytesToWeight(rawBytes)
    print(f"longWithOffsetValue: {longWithOffsetValue} | weight (grams): {weightValue}")

'''
About the reading format.
----------------
I've found out that, for some reason, the order of the bytes is not always the same between versions of python,
and the hx711 itself. I still need to figure out why.

If you're experiencing super random values, switch these values between `MSB` and `LSB` until you get more stable values.
There is some code below to debug and log the order of the bits and the bytes.

The first parameter is the order in which the bytes are used to build the "long" value. The second paramter is
the order of the bits inside each byte. According to the HX711 Datasheet, the second parameter is MSB so you
shouldn't need to modify it.
'''
hx.setReadingFormat("MSB", "MSB")

print("[INFO] Automatically setting the offset.")
hx.autosetOffset()
offsetValue = hx.getOffset()
print(f"[INFO] Finished automatically setting the offset. The new value is '{offsetValue}'.")

print("[INFO] You can add weight now!")

'''
# HOW TO CALCULATE THE REFFERENCE UNIT
1. Set the reference unit to 1 and make sure the offset value is set.
2. Load you sensor with 1kg or with anything you know exactly how much it weights.
3. Write down the 'long' value you're getting. Make sure you're getting somewhat consistent values.
    - This values might be in the order of millions, varying by hundreds or thousands and it's ok.
4. To get the wright in grams, calculate the reference unit using the following formula:  
    referenceUnit = longValueWithOffset / 1000
'''

referenceUnit = -8453
print(f"[INFO] Setting the 'referenceUnit' at {referenceUnit}.")
hx.setReferenceUnit(referenceUnit)
print(f"[INFO] Finished setting the 'referenceUnit' at {referenceUnit}.")

while True:
    try:
        getRawBytesAndPrintAll()
            
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        print("[INFO] 'KeyboardInterrupt Exception' detected. Cleaning and exiting...")
        sys.exit()
