import board
import neopixel
import time
import touchio
import adafruit_vl53l1x
import pwmio
import digitalio

strip_pin=board.A1
strip_num_of_lights=56
strip=neopixel.NeoPixel(strip_pin, strip_num_of_lights, brightness=0.5, auto_write=True)

i2c = board.I2C()
distance_sensor = adafruit_vl53l1x.VL53L1X(i2c)
distance_sensor.distance_mode = 1
distance_sensor.timing_budget = 100

#begin sensor
distance_sensor.start_ranging()

touchpad_A6 = touchio.TouchIn(board.A6)
touchpad_A3 = touchio.TouchIn(board.A3)

def light_up(color):
    for i in range(strip_num_of_lights):
        strip[i]= ((color))
        time.sleep(0.05)
        
def light_up1(color1, color2):
    for i in range(strip_num_of_lights):
        if i%2 == 0:
            strip[i] = ((color1))
            time.sleep(0.05)
        else:
            strip[i]= ((color2))
            time.sleep(0.05)
    
while True:
    if touchpad_A6.value:
        light_up((255,0,0))
        strip.fill((0,0,0))
        #if the touchpad has been pressed
    elif touchpad_A3.value:
        strip.fill((255,255,0))
        strip.fill((0,0,0))
        #if the touchpad has been pressed
    elif distance_sensor.data_ready:
        #if the slider has been moved
        distance = distance_sensor.distance
        light_up1((255,255,0), (255,0,0))
        print(distance)
    
