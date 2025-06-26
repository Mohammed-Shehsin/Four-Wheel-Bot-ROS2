from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Start Gazebo server in headless mode with ROS factory plugin
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so', '--headless-rendering'],
            output='screen'
        ),
        # Spawn your robot entity into Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'four_wheel_bot',
                '-topic', 'robot_description'
            ],
            output='screen'
        )
    ])
