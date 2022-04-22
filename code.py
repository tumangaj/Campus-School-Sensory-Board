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
touchpad_A1 = touchio.TouchIn(board.A1)
touchpad_A3 = touchio.TouchIn(board.A3)
touchpad_TX = touchio.TouchIn(board.TX)

while True: 
    if touchpad_A1.value():
        #if the touchpad has been pressed
    if touchpad_A3.value():
        #if the touchpad has been pressed
    if distance_sensor.data_ready:
        #if the slider has been moved
        distance = distance_sensor.distance
        print(f"Distance: {distance}")
        time.sleep(0.1)
    
