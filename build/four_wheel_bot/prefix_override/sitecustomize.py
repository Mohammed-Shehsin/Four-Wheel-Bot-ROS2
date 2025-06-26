import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shehsin/ros2_ws/src/four_wheel_bot/install/four_wheel_bot'
