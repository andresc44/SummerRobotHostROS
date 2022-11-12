#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int64
import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

if __name__ == '__main__':
    rospy.init_node('ultrasonic_publisher')
    pubDistance = rospy.Publisher("/ultrasonic_distance", Float32, queue_size = 30)
    pubDrive = rospy.Publisher("/ultrasonic_drive_data", Int64, queue_size = 30)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        distanceOutput = Float32()
        driveCommand = Int64()

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        pulse_start = time.time()
        pulse_end = time.time()

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()


        pulse_duration = pulse_end-pulse_start
        distance=round(((34300*pulse_duration)/2),2)

        distanceOutput.data = distance

        driveCommand = 1
        if distance < 35:
            driveCommand = 2
        else:
            driveCommand = 1


        pubDistance.publish(distanceOutput)
        pubDrive.publish(driveCommand)
        rate.sleep()

    #rospy.loginfo("Node was stopped")
