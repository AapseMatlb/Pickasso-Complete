import rospy
from geometry_msgs.msg import Twist

def navigate_to_goal():
    rospy.init_node('navigation_node')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    move_cmd = Twist()
    move_cmd.linear.x = 0.2  # Forward speed
    move_cmd.angular.z = 0.0

    for _ in range(50):  # Move forward for some time
        pub.publish(move_cmd)
        rate.sleep()

    stop_cmd = Twist()
    pub.publish(stop_cmd)
    print("[Navigation] Goal Reached!")

if __name__ == "__main__":
    try:
        navigate_to_goal()
    except rospy.ROSInterruptException:
        pass
