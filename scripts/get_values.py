#! /usr/bin/env python
# Import libraries and messaging
import io
import csv
import rospy
import numpy as np
from numpy import inf
from numpy import asarray
from numpy import savetxt
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped

# Declare variables
i=0
global NewRanges

# Set desired target point
TP_x = -0.3
TP_y = 1.8

vel_x_linear = None
vel_z_angular = None

NewRanges = [''] * 90

# Write in .csv
csv_data = io.BytesIO()
csv_writer = csv.writer(csv_data)

# Create function to get and select the laser scan values of the mobile robot
def callback(msg):
	for i in range(90):
		NewRanges[i] = msg.ranges[i]
	
# Create function to get the linear velocity in x and the angular velocity in z of the mobile robot (tb3_0)
def callback2(msg):

	global vel_x_linear
	global vel_z_angular
	vel_x_linear = msg.linear.x
	vel_z_angular = msg.angular.z
	
# Create function to get the position x,y of the of the mobile robot (tb3_0)
def position_cb(msg):

	global x
	global y
	x = msg.pose.position.x
	y = msg.pose.position.y
	
# Initialize node
rospy.init_node('get_values')

# Subscribe to topics
sub1 = rospy.Subscriber('/tb3_0/new_scan', LaserScan, callback)
sub2 = rospy.Subscriber('/tb3_0/cmd_vel', Twist, callback2)
sub3 = rospy.Subscriber("/natnet_ros/tb0/pose", PoseStamped, position_cb)

# Create while loop
while not rospy.is_shutdown():

	# Store values in a .csv file every 0.2 seconds
	ros_rate = rospy.Rate(5) # 10Hz
	ros_rate.sleep()
	PrintVariable = NewRanges[:]
	PrintVariable.append(TP_x)
	PrintVariable.append(TP_y)
	PrintVariable.append(x)
	PrintVariable.append(y)
	PrintVariable.append(vel_x_linear)
	PrintVariable.append(vel_z_angular)
	if PrintVariable[0] != '':
	
		# Change the infinite values to max sensor distance range (3.5m)
		NN = np.array(PrintVariable)
		print(NN)
		with open('trainingDA.csv', 'a') as file:
			writer = csv.writer(file)
			writer.writerow(NN)
