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


with open('trainingDAB.csv', 'r') as old_file:
	csv_reader = csv.reader(old_file, delimiter=',')
	
	with open('trainingDAB_n.csv', 'w') as new_file:
		csv_writer = csv.writer(new_file)
		
		for row in csv_reader:
			if row != '':
				print(row)
				data = np.array(row, dtype=float)
				if data[0] >= 8.0:
					data[0] = 8.0
				for i in range(1,90):
					if data[i] <= 0.173:
						data[i] = data[i-1]
					elif data[i] >= 8.0:
						data[i] = data[i-1]
				csv_writer.writerow(data)
		
        	
		
