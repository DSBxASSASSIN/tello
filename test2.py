from djitellopy import Tello
import cv2 
import numpy as np 

me = Tello()
me.connect()

while True: 
    print(me.get_battery())