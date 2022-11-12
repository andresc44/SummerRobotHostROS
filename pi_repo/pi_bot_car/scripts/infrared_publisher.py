#!/usr/bin/env python3

import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import Int64


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
GPIO.setup(19, GPIO.IN)


if __name__ == '__main__':

    rospy.init_node('infrared_publisher')

    pubL = rospy.Publisher("/infraredLeft", Int64, queue_size = 10)
    pubR = rospy.Publisher("/infraredRight", Int64, queue_size = 10)
    pubFast = rospy.Publisher("/motorsFromInfrared", Int64, queue_size = 10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        left = Int64()
        right = Int64()
        motor = Int64()
        if (GPIO.input(16) == False) and (GPIO.input(19) == False):
            left.data = 1
            right.data = 1
            motor.data = 1
        elif (GPIO.input(16) == False) and (GPIO.input(19) == True):
            left.data = 0
            right.data = 1
            motor.data = 2
        elif (GPIO.input(16) == True) and (GPIO.input(19) == False):
            left.data = 1
            right.data = 0
            motor.data = 4
        else:
            left.data = 0
            right.data = 0
            motor.data = 0

        pubL.publish(left)
        pubR.publish(right)
        pubFast.publish(motor)
        rate.sleep()
    #rospy.loginfo("Node stopped")



