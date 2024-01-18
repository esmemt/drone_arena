#!/usr/bin/env python  

import rospy

import numpy as np 

import math 

from sensor_msgs.msg import LaserScan   


class NewLaserClass():  

	def __init__(self):  
		
		rospy.on_shutdown(self.cleanup)  
		
		NewRanges = [0] * 90
 

		################# SUBSCRIBERS ###################
		rospy.Subscriber("/tb3_0/scan", LaserScan, self.laser_cb) 
		pub = rospy.Publisher("/tb3_0/new_scan", LaserScan, queue_size = 1)
		
		############ CONSTANTS ################ 
		self.laser = LaserScan()
		
		r = rospy.Rate(5) #1Hz  
		sequence = 0
		print("Node initialized 1hz") 
		
		while not rospy.is_shutdown(): 

			if self.laser.ranges:
				angle_min = np.rad2deg(self.laser.angle_min) #In degrees
				angle_increment = np.rad2deg(self.laser.angle_increment) #Given in degrees
				j = 0
				count = 0
				
				for angle in range(270,360,2):
					index = int((angle - angle_min)/angle_increment)
					if index >= (len(self.laser.ranges) - 1):
						index = (len(self.laser.ranges) - 1)
					NewRanges[j] = self.laser.ranges[index]
					j += 1
					
				for angle in range(2,90,2):
					j += 1
					index = int((angle - angle_min)/angle_increment)
					NewRanges[j] = self.laser.ranges[index]
				
				for i in range(0,90):
					if NewRanges[0] == 0:
						for value in NewRanges:
							if value != 0:
								NewRanges[0] = value
								break
					if NewRanges[i] >= 8.0:
						NewRanges[i] = 8.0
					elif NewRanges[i] <= 0.16:
						NewRanges[i] = NewRanges[i - 1]
						
				new_scan = LaserScan()
				new_scan.header.frame_id = self.laser.header.frame_id
				new_scan.angle_min = -np.pi/2.0
				new_scan.angle_max = np.pi/2.0
				new_scan.angle_increment = np.deg2rad(2)
				new_scan.range_min = self.laser.range_min
				new_scan.range_max = self.laser.range_max
				new_scan.header.stamp = rospy.Time.now()
				new_scan.header.seq = sequence
				sequence +=1
				new_scan.ranges = NewRanges
					
				pub.publish(new_scan)		
			r.sleep()  

             

             

             

	def laser_cb(self, msg):  

		## This function receives a number   
		#For hls lidar  
		
		self.laser = msg

		 

         

	def cleanup(self):  

		#This function is called just before finishing the node  

		# You can use it to clean things up before leaving  

		# Example: stop the robot before finishing a node.    

		pass  

############################### MAIN PROGRAM ####################################  

if __name__ == "__main__":  

    rospy.init_node("laser_publisher", anonymous=True)  

    NewLaserClass() 
