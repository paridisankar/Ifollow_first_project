#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import String 

def talker(frequency_rate:int):
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)

    rate = rospy.Rate(frequency_rate)
    
    while not rospy.is_shutdown():
        hello_str = "%s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
    
        
if __name__ == '__main__':
    try:
        talker(int(sys.argv[1]))
    except rospy.ROSInterruptException:
        pass           
