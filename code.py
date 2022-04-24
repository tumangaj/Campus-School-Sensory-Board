import board
import neopixel
import time
import touchio
import adafruit_vl53l1x
import pwmio
import digitalio
from audiopwmio import PWMAudioOut as AudioOut
from audiocore import WaveFile

speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True
audio = AudioOut(board.SPEAKER)

strip_pin=board.A1
strip_num_of_lights=56
strip=neopixel.NeoPixel(strip_pin, strip_num_of_lights, brightness=0.5, auto_write=True)

path = "sounds/"

def play_sound(filename):
    with open(path + filename, "rb") as wave_file:
            wave = WaveFile(wave_file)
            audio.play(wave)
            while audio.playing:
                pass

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

#needs modification based on board-smaller values

def distance_colors(distance):
    if(distance <= 8 and distance>1):
        for i in range(56):
            strip[i]=((0,255,255))
    elif(distance>8 and distance <= 13):
        for i in range(45):
            strip[i]=((0,255,255))
        for x in range(45, 56):
            strip[x]= ((0,0,0))
    elif(distance>13 and distance <= 15):
        for i in range(30):
            strip[i]=((0,255,255))
        for x in range(30, 56):
            strip[x]= ((0,0,0))
    elif(distance>15 and distance <= 19):
        for i in range(15):
            strip[i]=((0,255,255))
        for x in range(31, 56):
            strip[x]= ((0,0,0))
    elif(distance>19 or distance==0):
       strip.fill((0,0,0))
    
    
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
        distance_colors(distance)
        print(distance)
    
