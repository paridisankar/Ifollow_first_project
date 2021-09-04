#include "ros/ros.h"
#include "std_msgs/String.h"


double avg_time_difference = 0.0;
double total_time = 0.0;
double count = 1;

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{

    std::stringstream ss;

    double publisher_time = std::stod(msg->data.c_str());
    ss << "" << ros::Time::now();
    double subscriber_time = std::stod(ss.str().c_str());
    
    double  current_time_difference = subscriber_time - publisher_time;
        
    // calculating average time differences between subscriber time and publisher time
    total_time = current_time_difference + total_time;
    avg_time_difference = total_time / count;


    ROS_INFO("\t current_time_difference: %lf", current_time_difference);
    ROS_INFO("\t avg_time_difference: %lf", avg_time_difference);
  
    // counting the number of subscribed messages
    count++;
  
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "listener");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
  ros::spin();

  return 0;
}
