#!/usr/bin/env python  

import rospy

from geometry_msgs.msg import PoseStamped

# This class will subscribe to the /pose topic and print some data 

class ArenaSubClass():  

    def __init__(self):  

        rospy.on_shutdown(self.cleanup)  

        ############    SUBSCRIBERS   #######################  

        rospy.Subscriber("/natnet_ros/tb0/pose", PoseStamped, self.position_cb)  

        ############ CONSTANTS AND VARIABLES ################  

        self.apose = PoseStamped() #The data from the arena will be kept here. 

        r = rospy.Rate(1) #1Hz  

        print("Node initialized 1hz") 

         

        while not rospy.is_shutdown():  

            print("position x:") 

            print(self.apose.pose.position.x) 
            
            print("position y:")
            
            print(self.apose.pose.position.y)

            r.sleep()  #It is very important that the r.sleep function is called at least once every cycle.  

     

    def position_cb(self, arena_pose):  

        ## This function receives the lidar message and copies this message to a member of the class  

        self.apose = arena_pose 

 

         

         

    def cleanup(self):  

        #This function is called just before finishing the node  

        # You can use it to clean things up before leaving  

        # Example: stop the robot before finishing a node.    

        print("I'm dying, bye bye!!!")  

 

############################### MAIN PROGRAM ####################################  

if __name__ == "__main__":  

    rospy.init_node("pose_stamped_subscriber", anonymous=True)  

    ArenaSubClass()
    

