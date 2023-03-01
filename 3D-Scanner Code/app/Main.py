#!/usr/bin/python3

import time
from picamera2 import Picamera2
from libcamera import controls
from routers import motors
from controllers import motors
from models.motor import MotorType
from config import config


#move_motor_degrees(Motor.turntable, 30)
def get_motors():
    return motors.get_motors()
def get_motor(motor_type: MotorType):
    return motors.get_motor(motor_type)

def move_motor(motor_type: MotorType, degrees: float):
    motor = motors.get_motor(motor_type)
    motors.move_motor_degrees(motor, degrees)
    
    
    

    

def Foto(x,y):
    
    picam2.start_and_capture_files("Ebene"+str(x)+"Bild"+str(y)+"{:d}.jpg", num_files=1, delay=0.5)
    #print("Ebene"+str(x)+"Bild"+str(y))
    time.sleep(2)
    
    
def Schritt1():
    move_motor(MotorType("turntable"),360/25)
    print("Schritt1")
    time.sleep(2)
    
    
def Schritt2():
    move_motor(MotorType("rotor"),2)
    print("Schritt2")
    
def Loop1(x,y):
    for i in range(5):
        Foto(x,y)
        Schritt1()
        y=y+1
        
    y=y+1
    Foto(x,y)
    return x , y
def Loop2(x,y):
    
    for i in range(2):
        picam2.start(show_preview=True)
        picam2.set_controls({"AfMode": 1, "AfTrigger": 0})
        time.sleep(15)
        Loop1(x,y)
        Schritt2()
        x=x+1

get_motors()
get_motor(MotorType("turntable"))
get_motor(MotorType("rotor"))




x = 1
y = 1




#move_motor(MotorType("turntable"),1)
#move_motor(MotorType("rotor"),1)

picam2 = Picamera2()


#show_preview=True
#"AfMode": 2, "AfTrigger": 0
#"AfMode": controls.AfModeEnum.Continuous,
# Manueller Autofocus :"AfMode": 0, "LensPosition": 6.5
# Autofocus speed : "AfSpeed": controls.AfSpeedEnum.Fast
#"AfMode": controls.AfModeEnum.Continuous
#Af mode 2 "AfMode": 2, "AfTrigger": 0
#"AfMode": controls.AfModeEnum.Continuous,"AfSpeed": controls.AfSpeedEnum.Fast



Loop2(x,y)