#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import random

def node():
    rospy.init_node('micro_node')
    pub = rospy.Publisher('/sensor/sound', Float32, queue_size=10)
    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        value = Float32()
        value.data = 30 + random.uniform(-10,10)  # dB simulé
        pub.publish(value)
        rospy.loginfo(f"Son simulé: {value.data:.1f} dB")
        rate.sleep()

if __name__ == "__main__":
    try:
        node()
    except rospy.ROSInterruptException:
        pass
