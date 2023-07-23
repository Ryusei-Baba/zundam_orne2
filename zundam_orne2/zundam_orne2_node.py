# SPDX-FileCopyrightText: 2023 Ryusei Baba <babaryusei.kw@gmail.com>
# SPDX-License-Identifier: BSD 3-Clause

import rclpy
import time
import os
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from playsound import playsound


class ZundamSubscriber(Node): 
    def __init__(self):
        super().__init__('zundam_subscriber_node') 
        self.subscription = self.create_subscription(Twist,'cmd_vel', self.callback, 10)
        self.vel = Twist()
               
    def callback(self, Twist): 
        if Twist.linear.x > 0.2:
            playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/001_ずんだもん（ノーマル）_ロボットが動くのだ.wav"))
        return Twist
        # self.get_logger().info("Velocity: Linear=%f angular=%f" % (Twist.linear.x,Twist.angular.z)) 
   
   
def main():
    rclpy.init()
    node = ZundamSubscriber()
    try:
        rclpy.spin(node) 
    except KeyboardInterrupt:
        print("Ctrl+C が押されました．")
    finally:
        rclpy.shutdown()
        print('プログラム終了')
# def main(args=None):
#     rclpy.init(args=args)
#     node = ZundamSubscriber()
#     rclpy.spin(node)
#     node.destory_node()
#     rclpy.shutdown()
