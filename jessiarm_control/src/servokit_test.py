#!/usr/bin/python

from time import sleep

# Import the PCA9685 module.
import Adafruit_PCA9685
from Adafruit_GPIO import I2C
import myconfig as mc

def get_bus():
    return 1

I2C.get_default_bus = get_bus

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
channel = 0

# Set home position
pwm.set_pwm(0, 1,  mc.MOTOR1_HOME)       
pwm.set_pwm(0, 2,  mc.MOTOR2_HOME)  
pwm.set_pwm(0, 3,  mc.MOTOR3_HOME) 
pwm.set_pwm(0, 14, mc.MOTOR4_HOME)
pwm.set_pwm(0, 15, mc.GRIPPER_HOME)
pwm.set_pwm(0, 0,  mc.MOTOR0_HOME) 

while True:
    try:
        user_input = raw_input('Channel 0~15: ')
    except KeyboardInterrupt:
       break
    except:
       continue        
    if user_input:
        channel = int(user_input)
    
    try:
        pulse = raw_input("Insert position:")
    except KeyboardInterrupt:
       break
    except:
       continue
    i=int(pulse)
    pwm.set_pwm(channel,0,i)

print("servo test done,release pca9685")
pwm.set_all_pwm(0,0)
