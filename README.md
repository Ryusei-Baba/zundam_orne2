# zundam_ros2
ROS 2です．Topicを受け取るとずんだもんが喋ります．</br>
クレジット　VOICEVOX:ずんだもん [VOICEVOX 公式ページ](https://voicevox.hiroshiba.jp/)</br>


## install
```
pip3 install playsound
cd ~/ws/src/
git clone https://github.com/Ryusei-Baba/zundam_orne2.git
cd ~/ws/
colcon build --symlink-install
source install/setup.bash
```

## run
```
ros2 run zundam_orne2 zundam_orne2_node
```
