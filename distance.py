from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24, max_distance=4)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)
