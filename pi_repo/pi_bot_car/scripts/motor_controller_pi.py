#!/usr/bin/env python3

import rospy
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT) #left motor
GPIO.setup(17, GPIO.OUT) #left motor
GPIO.setup(27, GPIO.OUT) #right motor
GPIO.setup(22, GPIO.OUT) #right motor

GPIO.setup(13, GPIO.OUT) #left enable pin
GPIO.setup(21, GPIO.OUT) #right enable pin
pwm_left = GPIO.PWM(13,100) #enable left pin as pwm
pwm_right = GPIO.PWM(21, 100) #^^^
pwm_left.start(50) #left motor starts with 50%
pwm_right.start(50)#right motor starts at 50%
GPIO.output(13, True)
GPIO.output(21, True)
from std_msgs.msg import Int64

def callback_receive_motor_data(direction):
    if direction.data == 2: #she go right
        pwm_left.ChangeDutyCycle(40)
        pwm_right.ChangeDutyCycle(40)
        GPIO.output(18, True)
        GPIO.output(17, False)
        GPIO.output(27, False)
        GPIO.output(22, True)
        rospy.loginfo("Right")
    elif direction.data == 1: #she go forward
        pwm_left.ChangeDutyCycle(33)
        pwm_right.ChangeDutyCycle(33)
        GPIO.output(18, True)
        GPIO.output(17, False)
        GPIO.output(27, True)
        GPIO.output(22, False)
        rospy.loginfo("Forward")
    elif direction.data == 4: #she go left
        pwm_left.ChangeDutyCycle(40)
        pwm_right.ChangeDutyCycle(40)
        GPIO.output(18, False)
        GPIO.output(17, True)
        GPIO.output(27, True)
        GPIO.output(22, False)
        rospy.loginfo("Left")
    elif direction.data == 3: #she go back
        pwm_left.ChangeDutyCycle(33)
        pwm_right.ChangeDutyCycle(33)
        GPIO.output(18, False)
        GPIO.output(17, True)
        GPIO.output(27, False)
        GPIO.output(22, True)
        rospy.loginfo("Backwards")
    else:
        pwm_left.ChangeDutyCycle(0)
        pwm_right.ChangeDutyCycle(0)
        GPIO.output(18, False)
        GPIO.output(17, False)
        GPIO.output(27, False)
        GPIO.output(22, False)



if __name__ == '__main__':

    rospy.init_node('motor_controller_pi')

    sub = rospy.Subscriber("/motor_commands", Int64, callback_receive_motor_data)

    rospy.spin()

