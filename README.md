# zundam_ros2
ROS 2です．Topicを受け取るとずんだもんが喋ります．</br>
クレジット　VOICEVOX:ずんだもん [VOICEVOX 公式ページ](https://voicevox.hiroshiba.jp/)</br>


## install
```
pip3 install playsound
git clone
cd ~/ws/
rosdep install -i --from-path src -y
colcon build --symlink-install
source install/setup.bash
```
