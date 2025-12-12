#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import random

def node():
    rospy.init_node('test_dht11_node')
    pub = rospy.Publisher('/test/temperature', Float32, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz (1 fois par seconde)

    while not rospy.is_shutdown():
        value = Float32()
        value.data = 20 + random.uniform(-2,2)  # valeur simulée
        pub.publish(value)
        rospy.loginfo(f"Temp: {value.data}")
        rate.sleep()

if __name__ == "__main__":
    try:
        node()
    except rospy.ROSInterruptException:
        pass
