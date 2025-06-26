from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

import os

def generate_launch_description():
    pkg_name = 'four_wheel_bot'
    pkg_share = FindPackageShare(pkg_name)
    xacro_file = PathJoinSubstitution([pkg_share, 'urdf', 'robot.urdf.xacro'])

    return LaunchDescription([
        # Launch Gazebo empty world
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'])
            ])
        ),

        # Robot State Publisher with xacro
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command([FindExecutable(name='xacro'), ' ', xacro_file])
            }]
        ),

        # Spawn entity into Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-topic', 'robot_description', '-entity', 'four_wheel_bot'],
            output='screen'
        ),
    ])
