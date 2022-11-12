#!/usr/bin/env python3

import rospy
import gpiozero
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int64

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
beep = 5
GPIO.setup(beep, GPIO.OUT)

def callback_receive_sound_flex_data(sound):
    if sound.data  == 1:
        GPIO.output(beep, True)
    else:
        GPIO.output(beep, False)

if __name__ == '__main__':

    rospy.init_node('good_listener')

    sub = rospy.Subscriber("/sound_flex", Int64, callback_receive_sound_flex_data)

    rospy.spin()

