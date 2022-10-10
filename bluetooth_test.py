#!/usr/bin/env python3
 
 
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
  while(True):
    try:
      # Keep reading data from the robot
      incoming_data_from_robot = pc_bluetooth_handle.recv(
                      data_size)
      time.sleep(0.1) #this is the originial time.sleep to keep later
      
      #print("This is the length: ", len(incoming_data_from_robot))
      incoming_data_from_robot = str(incoming_data_from_robot)
      length = len(incoming_data_from_robot)
      #indexN = incoming_data_from_robot[10]
      #print(indexN)

      if length == 12:
          indexN = incoming_data_from_robot[10]
          if indexN == 'n':
              #print("This is the perfect message when length is 12: ", incoming_data_from_robot)
              valG = incoming_data_from_robot[2]
              valP = incoming_data_from_robot[3]
              valR = incoming_data_from_robot[4]
              valM = incoming_data_from_robot[5]
              valI = incoming_data_from_robot[6]
              print("Value G is: ", valG,"Value P is: ", valP,"Value R is: ", valR,"Value M is: ", valM,"Value I is: ", valI)
      #print("Value P is: ", valP)
      #print("Value R is: ", valR)
      #print("Value M is: ", valM)
      #print("Value I is: ", valI)
      incoming_data_from_robot = None
      #valG = None
      #valP = None
      #valR = None
      #valM = None
      #valI = None
    except bluetooth.btcommon.BluetoothError as error:
      print ("Caught BluetoothError: ", error)
      time.sleep(5)
      pc_bluetooth_handle = connect()
      pass
 
  pc_bluetooth_handle.close()
