from adafruit_circuitplayground import cp
import time

while True:
    temp1=cp.temperature
    print(str(temp1) + 'F')
    #serial.write_line(str(temp1))
    cp.red_led = cp.button_b
    time.sleep(4)
