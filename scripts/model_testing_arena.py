#! /usr/bin/env python

# Import libraries and messaging
import keras
import rospy
import numpy as np
import tensorflow as tf
from numpy import inf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped
from tensorflow.keras.models import load_model

# Load neural network model
model = load_model('trainingDA.h5')

# Summarize model
model.summary()

# Declare variables
i=0
global NewRanges
vel_x_linear = None
vel_z_angular = None
NewRanges = [''] * 90

# Set desired target point
TP_x = -0.3
TP_y = 1.8

x = 0.0
y = 0.0

# Create function to get and select the laser scan values of the mobile robot
def callback(msg):
	for i in range(90):
		NewRanges[i] = msg.ranges[i]
	
# Create function to get the position x,y of the of the mobile robot (tb3_0)
def newOdom(msg):

	global x
	global y
	x = msg.pose.position.x
	y = msg.pose.position.y

# Initialize node
rospy.init_node('testing')

# Subscribe to topics
sub1 = rospy.Subscriber('/tb3_0/new_scan', LaserScan, callback)
sub2 = rospy.Subscriber("/natnet_ros/tb0/pose", PoseStamped, newOdom)

speed = Twist()

# Publish to topics
pub = rospy.Publisher('/tb3_0/cmd_vel', Twist, queue_size = 1)

# Create while loop
while not rospy.is_shutdown():
	
	# Get laser values every 0.2 seconds
	ros_rate = rospy.Rate(5) # 5Hz
	ros_rate.sleep()
	if NewRanges[0] != '':
		NN = np.array(NewRanges)
		TPX = np.array(TP_x)
		TPY = np.array(TP_y)
		LTPX = np.append(NN,TPX)
		LTPXTPY = np.append(LTPX,TPY)
		IPX = np.array(x)
		IPY = np.array(y)
		LTPXTPYIPX = np.append(LTPXTPY,IPX)
		LTPXTPYIPXIPY = np.append(LTPXTPYIPX,IPY)
		New = LTPXTPYIPXIPY.reshape(1, 1, LTPXTPYIPXIPY.shape[0])
		print("Target Point:", TP_x, TP_y)
		print("Current Point:", x, y)
		ypredreal = model.predict(New)
		print("Predicted linear and angular velocity:", ypredreal)
		# Publish predicted linear and angular speed on Twist
		speed.linear.x = ypredreal[0,0]
		speed.angular.z = ypredreal[0,1]
		pub.publish(speed)
