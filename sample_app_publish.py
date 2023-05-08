#!/usr/bin/env python3
#-*- coding:utf-8 -*-	# 한글 주석을 달기 위해 사용한다.


''' azure에서 보내는 publish 정보
        std_msgs::Float32 msg;
        msg.data = 0;
        pub.publish(msg);

TrackerNode::TrackerNode(ros::NodeHandle& _nh)
{
	nh=_nh;
	lengthPub = nh.advertise<std_msgs::Float32>("length",1000);	
}


OpenCR 에서 보내는 정보     

ros::Publisher sceinaro_make("bookcase_num",  &moter_num)
std_msgs::String moter_num //string type으로 bookcase_num topic날림

'''

import rospy
from std_msgs.msg import Float32, String, Int16


class app:
    def __init__(self):

        self.bookcase_num = None
        self.bookcase = ["book 1", "book 2","book 3","book 4", "book 5", "book 6","book 7","book 8","book 9"]


        rospy.init_node('sceinaro_node', anonymous=True)
        self.publisher1 = rospy.Publisher('bookcase_num', String, queue_size=10)
        self.publisher2 = rospy.Publisher('count', Int16, queue_size=10)



        self.rate = rospy.Rate(30) # 0.5hz


    def app_publish(self):

        count = 0
        idx = 0
        while not rospy.is_shutdown(): #-> c++에서 ros.ok() 느낌
            self.publisher1.publish(self.bookcase[idx])
            if self.bookcase[idx] == self.bookcase[-1]:
                idx = 0
            else:
                pass
            
            self.publisher2.publish(count)
            if count >3:
                count = 0
            else:
                pass

            rospy.loginfo(count , self.bookcase[idx]) 
            
            self.rate.sleep() #100hz가 될때 까지 쉬기

            


if __name__ == '__main__':
    try:
        a = app()
        a.app_publish()
    except rospy.ROSInterruptException:
        pass
