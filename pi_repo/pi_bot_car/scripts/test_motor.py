#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

if __name__ == '__main__':

    rospy.init_node('motor_tester', anonymous = True)

    pub = rospy.Publisher("/motor_commands", Int64, queue_size=10)

    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        motor_instruction = Int64()
        motor_instruction.data = 1
        pub.publish(motor_instruction)
        rate.sleep()
    #rospy.loginfo("Node stopped")
