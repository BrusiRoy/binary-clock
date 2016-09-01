# Bruno Roy 2016/09/01
# Binary Clock for Raspberry Pi 1
# Using SN74HC595 shift registers

import time
import RPi.GPIO as GPIO

# GPIO pins set up
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)  # SER   (serial-in)
GPIO.setup(10, GPIO.OUT) # RCLK  (storage register clock)
GPIO.setup(12, GPIO.OUT) # SRCLK (shift register clock)

# Convert time from a decimal representation to binary
def convertToBinary(decimalTime):
    number = "00"
    for i, c in enumerate(decimalTime):
        if i % 2 == 0:
            number += bin(int(c))[2:].rjust(3, "0")
        else:
            number += bin(int(c))[2:].rjust(4, "0")
    return number

# Convert a string of "1" and "0" to a serial inpupt for the shift registers
def writeReg(number):
    GPIO.output(10, False)
    for x in number:
        GPIO.output(12, False)
        if x == "1":
            GPIO.output(8, True)
        else:
            GPIO.output(8, False)
        GPIO.output(12, True)
    GPIO.output(10, True)

print("Clock Starting")
while True:
    timeNow = time.strftime("%H%M")
    writeReg(convertToBinary(timeNow))
    time.sleep(5) # Only check the time every 5 seconds
