
#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import random

# Sur PC on simule
USE_REAL_SENSOR = True

# Initialisation ROS
rospy.init_node('dht11_node')
pub_temp = rospy.Publisher('/sensor/temperature', Float32, queue_size=10)
pub_hum = rospy.Publisher('/sensor/humidity', Float32, queue_size=10)

rate = rospy.Rate(1)  # 1 Hz

while not rospy.is_shutdown():
    if USE_REAL_SENSOR:
        # Sur PC pas de capteur → rien à faire
        temperature = 20
        humidity = 50
    else:
        temperature = 20 + random.uniform(-2,2)
        humidity = 50 + random.uniform(-5,5)

    pub_temp.publish(temperature)
    pub_hum.publish(humidity)
    rospy.loginfo(f"T: {temperature:.1f} °C, H: {humidity:.1f} %")
    rate.sleep()
