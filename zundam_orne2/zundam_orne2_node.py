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
        self.flg = 0
               
    def callback(self, Twist): 
        if self.flg == 0:
            if Twist.linear.x == 0.0:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/004_ずんだもん（ノーマル）_どいてニャーーーー….wav"))
                self.flg = 1
                return Twist
            elif Twist.linear.x > 0.2 and Twist.angular.z < 0.2 and Twist.angular.z > -0.2:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/001_ずんだもん（ノーマル）_まっすぐ進むのだ.wav"))
                self.flg = 1
                return Twist
            elif Twist.angular.z <= -0.2:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/002_ずんだもん（ノーマル）_右に曲がるのだ.wav"))
                self.flg = 1
                return Twist
            elif Twist.angular.z >= 0.2:
                playsound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../src/zundam_orne2/voice/003_ずんだもん（ノーマル）_左に曲がるのだ.wav"))
                self.flg = 1
                return Twist
            else:
                return Twist
        elif self.flg == 1:
            time.sleep(5)    # default5秒
            self.flg = 0
            return Twist

   
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
