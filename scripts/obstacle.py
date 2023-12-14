#! /usr/bin/env python

# Import libraries and messaging
import time
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist

# Initialize node
rospy.init_node('speed_controller')

# Subscribe and publish to topics
pub = rospy.Publisher('/tb3_1/cmd_vel', Twist, queue_size = 1)

speed = Twist()
r = rospy.Rate(10) #10Hz

# Sleep
time.sleep(4.5)
speed.linear.x = 0.18

def stop_callback(event):
    rospy.signal_shutdown("Just stopping publishing...")

time = float(18) 
rospy.Timer(rospy.Duration(time), stop_callback)

# Create while loop
while not rospy.is_shutdown():

	pub.publish(speed)
	r.sleep()
