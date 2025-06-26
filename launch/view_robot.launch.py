from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    urdf_path = PathJoinSubstitution([
        FindPackageShare("four_wheel_bot"),
        "urdf",
        "robot.urdf.xacro"
    ])

    return LaunchDescription([
        # Joint State Publisher (publishes fake joint states)
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
        ),

        # Robot State Publisher (publishes TF tree from URDF)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', urdf_path])
            }]
        ),

        # RViz2 (for visualization)
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
        )
    ])

