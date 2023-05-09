#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    # Modify the message data
    data.data = "Cliven"
    # Publish the modified message to the 'name' topic
    pub.publish(data)

if name == 'main':
    # Initialize the node
    rospy.init_node('changeMSG', anonymous=True)

    # Subscribe to the 'chatter' topic and set the callback function
    rospy.Subscriber("chatter", String, callback)

    # Publish to the 'name' topic
    pub = rospy.Publisher('name', String, queue_size=10)

    # Prevent the node from exiting
    rospy.spin()
