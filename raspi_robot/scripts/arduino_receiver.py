#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
import bluetooth
import time

##################################################
# Bluetooth parameters

robot_bluetooth_mac_address = '00:14:03:06:10:EA'
port = 1
pc_bluetooth_handle = None
data_size = 600

######################################################
# Connect the PC's Bluetooth to the robot's Bluetooth

def connect():
  global pc_bluetooth_handle

  while(True):
    try:
      pc_bluetooth_handle = bluetooth.BluetoothSocket(
               bluetooth.RFCOMM)
      pc_bluetooth_handle.connect((
              robot_bluetooth_mac_address, port))
      break;
    except bluetooth.btcommon.BluetoothError as error:
      pc_bluetooth_handle.close()
      print (
         "Could not connect: ", error, "; Retrying in 10s...")
      time.sleep(10)

  return pc_bluetooth_handle

# Connect to the robot's Bluetooth  
pc_bluetooth_handle = connect()

#############################################################
# Main code

# If this file is the main (driver) program you are executing
if __name__ == '__main__':

    rospy.init_node('arduino_receiver')

    pubG = rospy.Publisher("/gyro", Int64, queue_size=10)
    pubP = rospy.Publisher("/light_flex", Int64, queue_size=10)
    pubR = rospy.Publisher("/sound_flex", Int64, queue_size=10)
    pubM = rospy.Publisher("/middle", Int64, queue_size=10)
    pubI = rospy.Publisher("/index", Int64, queue_size=10)

    rate = rospy.Rate(5)

#the orininal while was while(True) here

    while not rospy.is_shutdown():
        intValG = Int64()
        intValP = Int64()
        intValR = Int64()
        intValM = Int64()
        intValI = Int64()

        try:
            # Keep reading data from the robot
            incoming_data_from_robot = pc_bluetooth_handle.recv(data_size)
            time.sleep(0.1) #this is the originial time.sleep to keep later


      #print("This is the length: ", len(incoming_data_from_robot))
            incoming_data_from_robot = str(incoming_data_from_robot)
            length = len(incoming_data_from_robot)
            if length == 12:
                indexN = incoming_data_from_robot[10]
                if indexN == 'n':
                #print("This is the perfect message when length is 12: ", incoming_data_from_robot)
                    valG = int(incoming_data_from_robot[2])
                    valP = int(incoming_data_from_robot[3])
                    valR = int(incoming_data_from_robot[4])
                    valM = int(incoming_data_from_robot[5])
                    valI = int(incoming_data_from_robot[6])
                
                    intValG.data = valG
                    intValP.data = valP
                    intValR.data = valR
                    intValM.data = valM
                    intValI.data = valI

                    pubG.publish(intValG)
                    pubP.publish(intValP)
                    pubR.publish(intValR)
                    pubM.publish(intValM)
                    pubI.publish(intValI)

                #rospy.loginfo("Value G is: ", valG,"Value P is: ", valP,"Value R is: ", valR,"Value M is: ", valM,"Value I is: ", valI)
            incoming_data_from_robot = None
        except bluetooth.btcommon.BluetoothError as error:
            #print ("Caught BluetoothError: ", error)
            time.sleep(5)
            pc_bluetooth_handle = connect()
            pass
    rospy.loginfo("Node is stopped")
    pc_bluetooth_handle.close()
