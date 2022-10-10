#include <ros/ros.h>

int main (int argc, char **argv){
	ros::init(argc, argv, "my_first_cpp_node");
	ros::NodeHandle nh;

	ROS_INFO("Node started already, you slow smh");

	ros::Rate rate(10);

	while (ros::ok()){
		ROS_INFO("I hate this game");
		rate.sleep();
	}
}
