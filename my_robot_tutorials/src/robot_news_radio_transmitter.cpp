#include <ros/ros.h>
#include <std_msgs/String.h>

int main (int argc, char **argv){
	ros::init(argc, argv, "robot_news_radio_transmitter");
	ros::NodeHandle nh;

	ros::Publisher pub = nh.advertise<std_msgs::String>("/robot_news_radio", 10);
	
	double publish_frequency;
	nh.getParam("/number_publish_frequency", publish_frequency);
	ros::Rate rate (publish_frequency);

	while (ros::ok()){
		std_msgs::String msg;
		msg.data = "You know you love me, XOXO, Stupid Bitch :)";
		pub.publish(msg);
		rate.sleep();
	}
	
}
