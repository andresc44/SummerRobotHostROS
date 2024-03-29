#!/usr/bin/env python

import rospy
from rospy_tutorials.srv import AddTwoInts

if __name__ == '__main__':
    rospy.init_node("add_two_ints_client")
    
    rospy.wait_for_service("/add_two_ints")

    try:
        add_two_ints = rospy.ServiceProxy("/add_two_ints", AddTwoInts)
        response = add_two_ints(2, 3)
        rospy.loginfo("Sum is: " + str(response.sum))
    except rospy.ServiceException as e:
        rospy.logwarn("You did it wrong b: " + str(e))

