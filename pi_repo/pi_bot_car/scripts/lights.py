#!/usr/bin/env python3

import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import Int64

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

def callback_receive_light_flex_data(light):
    if light.data == 1:
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
    else:
        GPIO.output(25, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)

if __name__ == '__main__':

    rospy.init_node('light_subscriber')

    sub = rospy.Subscriber("/light_flex", Int64, callback_receive_light_flex_data)

    rospy.spin()
