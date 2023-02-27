#!/usr/bin/python3

import time
from picamera2 import Picamera2
from libcamera import controls
from routers import motors
from controllers.motors import move_motor_degrees


move_motor_degrees(MotorTURNTABLE, 30)


picam2 = Picamera2()
picam2.start(show_preview=True)
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous,"AfSpeed": controls.AfSpeedEnum.Fast})
# Manueller Autofocus :"AfMode": 0, "LensPosition": 6.5
# Autofocus speed : "AfSpeed": controls.AfSpeedEnum.Fast
#"AfMode": controls.AfModeEnum.Continuous
#Af mode 2 "AfMode": 2, "AfTrigger": 0
def Foto():
    #picam2.start_and_capture_files("fastfocus-test{:d}.jpg", num_files=2, delay=0.5)
     print("Foto")
def Schritt1():
    
    print("Schritt1")
def Schritt2():
    print("Schritt2")
def Loop1():
    for i in range(5):
        Foto()
        Schritt1()
    Foto()
def Loop2():
    for i in range(5):
        Loop1()
        Schritt2()
Loop2()