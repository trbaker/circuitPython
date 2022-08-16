# script uses Circuit Python 7.x on an AdaFruit Playground Express.
# Script reads temperature sensor data (F) and makes accessible via USB cable to host computer listening on serial port.

from adafruit_circuitplayground import cp
import time

while True:
    temp1=cp.temperature
    print(str(temp1) + 'F')
    time.sleep(10)
