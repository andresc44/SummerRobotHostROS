#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
if __name__ == '__main__':

    rospy.init_node('robot_news_radio_transmitter', anonymous = True)

    pub = rospy.Publisher("/robot_news_radio", String, queue_size=10)

    publish_frequency = rospy.get_param("/radio_publish_frequency")
    rate = rospy.Rate(publish_frequency)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "HI, this is Dan fromrfgmkegnk"
        pub.publish(msg)
        rate.sleep()
    rospy.loginfo("Node stopped")
