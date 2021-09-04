#!/usr/bin/env python
import rospy
from std_msgs.msg import String 

index = 1
avg_time_difference = 0.0
total_time = 0.0

def callback(data):
    global total_time
    global avg_time_difference
    global index
    
    current_time_difference = rospy.get_time() - float(data.data)
    total_time = current_time_difference + total_time
    avg_time_difference = total_time / index

    rospy.loginfo(rospy.get_caller_id() + ": %s - %s", rospy.get_time(), data.data)
    rospy.loginfo("\t current_time_difference: " + str(current_time_difference))
    rospy.loginfo("\t avg_time_difference: " + str(avg_time_difference))
    
    index = index + 1
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter",String, callback)
    rospy.spin()
    
    
if __name__ == '__main__':
    listener()
