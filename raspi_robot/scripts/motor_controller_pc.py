#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

middleFinger = 0
indexFinger = 0
FinalPiOrders = 0

def callback_receive_middle_data(middleFlex):
    global middleFinger
    middleFinger = middleFlex.data

def callback_receive_index_data(indexFlex):
    global indexFinger
    indexFinger = indexFlex.data

def callback_receive_gyro_data(gyroMotor):
    global FinalPiOrders
    if middleFinger == 0 and indexFinger == 0:
        FinalPiOrders = gyroMotor.data

def callback_receive_infrared_data(infraredMotor):
    global FinalPiOrders
    if middleFinger == 1 and indexFinger == 0:
        FinalPiOrders = infraredMotor.data

def callback_receive_ultrasonic_data(ultrasonicMotor):
    global FinalPiOrders
    if middleFinger == 0 and indexFinger == 1:
        FinalPiOrders = ultrasonicMotor.data



if __name__ == '__main__':

    rospy.init_node('motor_controller_pc')

    subMiddle = rospy.Subscriber("/middle", Int64, callback_receive_middle_data)
    subIndex = rospy.Subscriber("/index", Int64, callback_receive_index_data)
    subGyro = rospy.Subscriber("/gyro", Int64, callback_receive_gyro_data)
    subInfrared = rospy.Subscriber("/motorsFromInfrared", Int64, callback_receive_infrared_data)
    subUltrasonic = rospy.Subscriber("/ultrasonic_drive_data", Int64, callback_receive_ultrasonic_data)

    pub = rospy.Publisher("/motor_commands", Int64, queue_size=10)

    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        piMotor = Int64()
        piMotor.data = FinalPiOrders
        pub.publish(piMotor)
        rate.sleep()

