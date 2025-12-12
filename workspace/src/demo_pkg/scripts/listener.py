#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Received: %s" % msg.data)

rospy.init_node('listener')
rospy.Subscriber('chatter', String, callback)

rospy.spin()

