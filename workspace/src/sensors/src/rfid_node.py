#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import random

def node():
    rospy.init_node('rfid_node')
    pub = rospy.Publisher('/sensor/rfid', String, queue_size=10)
    rate = rospy.Rate(0.2)
    uids = ['UID123', 'UID456', 'UID789']
    while not rospy.is_shutdown():
        msg = String()
        msg.data = random.choice(uids)
        pub.publish(msg)
        rospy.loginfo(f"RFID simulé: {msg.data}")
        rate.sleep()

if __name__ == "__main__":
    try:
        node()
    except rospy.ROSInterruptException:
        pass
