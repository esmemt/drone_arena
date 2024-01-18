#!/usr/bin/env python  

import rospy  

from sensor_msgs.msg import LaserScan

# This class will subscribe to the /scan topic and print some data 

class LaserSubClass():  

    def __init__(self):  

        rospy.on_shutdown(self.cleanup)  

 

        ############    SUBSCRIBERS   #######################  

        rospy.Subscriber("scan", LaserScan, self.lidar_cb)  

        ############ CONSTANTS AND VARIABLES ################  

        self.lidar = LaserScan() #The data from the lidar will be kept here. 

        r = rospy.Rate(1) #1Hz  

        print("Node initialized 1hz") 

         

        while not rospy.is_shutdown():  

            """print("ranges:") 

            print(self.lidar.ranges) 
            
            print("angle_min:")
            
            print(self.lidar.angle_min)
            
            print("angle_max:")
            
            print(self.lidar.angle_max)
            
            print("range_min:")
            
            print(self.lidar.range_min)
            
            print("range_max:")
            
            print(self.lidar.range_max)
            
            print("header frame_id:")
            
            print(self.lidar.header.frame_id)"""
            
            """if len(self.lidar.ranges) != 0:
            	
            	print("ranges[0]:")
            
            	print(self.lidar.ranges[0])
            
            if len(self.lidar.intensities) != 0:
            
            	print("intensities")"""
            
            	
            print("ranges size:" +str(len(self.lidar.ranges)))
            print("angle_min: "+str(self.lidar.angle_min))
            print("angle_max: "+str(self.lidar.angle_max))
            print("angle_increment: "+str(self.lidar.angle_increment))
            print("-------------")
            """lim_l = len(self.lidar.ranges) - 1
            if len(self.lidar.ranges) != 0:
                       j = 0
                       NewRanges = [''] * 90
                       for i in range(44,-1,-1):
            		           NewRanges[i] = self.lidar.ranges[lim_l - j]
            		           if NewRanges[i] == 0.0:
            			           NewRanges[i] = 100.0
            		           j += 1
                       for i in range(45,90):
            		           NewRanges[i] = self.lidar.ranges[j]
            		           if NewRanges[i] == 0.0:
            			           NewRanges[i] = 100.0
            		           j += 1"""
            print()


            r.sleep()  #It is very important that the r.sleep function is called at least once every cycle.  

     

    def lidar_cb(self, lidar_msg):  

        ## This function receives the lidar message and copies this message to a member of the class  

        self.lidar = lidar_msg 


         

         

    def cleanup(self):  

        #This function is called just before finishing the node  

        # You can use it to clean things up before leaving  

        # Example: stop the robot before finishing a node.    

        print("I'm dying, bye bye!!!")  

 

############################### MAIN PROGRAM ####################################  

if __name__ == "__main__":  

    rospy.init_node("laser_scan_subscriber", anonymous=True)  

    LaserSubClass()
