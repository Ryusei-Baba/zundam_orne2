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
        self.subscription = self.create_subscription(Twist,'cmd_vel', self.callback, 1)
        self.create_timer(0.01, self.timer_callback)
        self.vel = Twist()
        self.flg = 0
        self.time = 0
               
    def timer_callback(self):
        self.time += 0.01

    def callback(self, Twist): 
        if self.time <= 5:
            if self.flg != 1 and Twist.linear.x == 0.0 and Twist.angular.z == 0.0:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/004_ずんだもん（ノーマル）_お休み中なのだ.wav"))
                self.flg = 1
                self.time = 0
                return Twist
            elif self.flg != 2 and Twist.linear.x > 0.2 and Twist.angular.z < 0.5 and Twist.angular.z > -0.5:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/001_ずんだもん（ノーマル）_まっすぐ進むのだ.wav"))
                self.flg = 2
                self.time = 0
                return Twist
            elif self.flg != 3 and Twist.angular.z <= -0.5:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/002_ずんだもん（ノーマル）_右に曲がるのだ.wav"))
                self.flg = 3
                self.time = 0
                return Twist
            elif self.flg != 4 and Twist.angular.z >= 0.5:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/003_ずんだもん（ノーマル）_左に曲がるのだ.wav"))
                self.flg = 4
                self.time = 0
                return Twist
        else:
            if self.flg == 1:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/004_ずんだもん（ノーマル）_お休み中なのだ.wav"))
                self.time = 0
                return Twist
            elif self.flg == 2:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/001_ずんだもん（ノーマル）_まっすぐ進むのだ.wav"))
                self.time = 0
                return Twist
            elif self.flg == 3:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/002_ずんだもん（ノーマル）_右に曲がるのだ.wav"))
                self.time = 0
                return Twist
            elif self.flg == 4:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/003_ずんだもん（ノーマル）_左に曲がるのだ.wav"))
                self.time = 0
                return Twist
        
        self.get_logger().info("Velocity: Linear=%f angular=%f" % (Twist.linear.x,Twist.angular.z))

   
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
