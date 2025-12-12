#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('chatter', String, queue_size=10)

rate = rospy.Rate(1)

while not rospy.is_shutdown():
    msg = "Hello from Docker ROS!"
    rospy.loginfo(msg)
    pub.publish(msg)
    rate.sleep()


