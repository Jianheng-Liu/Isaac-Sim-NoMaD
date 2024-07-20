from isaacsim import SimulationApp
# 初始化Isaac Sim
simulation_app = SimulationApp({"headless": False})

from omni.isaac.core import World
from omni.isaac.core.utils.stage import open_stage

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import numpy as np


open_stage(usd_path='/home/jianheng/omniverse/assets/Warehouse_01.usd')
world = World()

# 加载机器人
robot_path = '/home/jianheng/omniverse/assets/Turtlebot3_Camera.usd'  # 你的机器人模型路径
robot_prim = world.stage.DefinePrim(robot_path, "Robot")
world.add(robot_prim)

# 获取机器人内置的相机
camera = robot_prim.get_camera("camera")  # 替换 'camera_name' 为USD文件中相机的实际名称

# 为机器人添加控制器
controller = robot_prim.add_controller("diff_drive", params={"wheel_base": 0.5})

# 重置世界以更新物理属性
world.reset()

# 初始化ROS节点
rospy.init_node('isaac_ros_bridge')

# 发布机器人传感器数据
camera_publisher = rospy.Publisher("/camera_topic", Image, queue_size=10)
def publish_camera_data():
    image = camera.get_color_rgba()
    ros_image = Image()
    ros_image.height = image.shape[0]
    ros_image.width = image.shape[1]
    ros_image.encoding = "rgba8"
    ros_image.data = image.flatten().tolist()
    camera_publisher.publish(ros_image)

# 订阅键盘控制命令
cmd_vel_subscriber = rospy.Subscriber("/cmd_vel", Twist, lambda msg: controller.set_linear_angular_speed(msg.linear.x, msg.angular.z))

# 主循环
while not rospy.is_shutdown():
    world.step(render=True)
    publish_camera_data()
