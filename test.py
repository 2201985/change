import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    # Modify the message
    change_str = "content: " + data.data

    # Publish the modified message
    pub = rospy.Publisher('chatter_modified', String, queue_size=10)
    pub.publish(change_str)

def message_modifier():
    rospy.init_node('message_modifier', anonymous=True)
    rospy.Subscriber("chatter", String, callback)

    rospy.spin()

if __name__ == '__main__':
    message_modifier()