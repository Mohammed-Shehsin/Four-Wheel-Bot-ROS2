from setuptools import setup
import os
from glob import glob

package_name = 'four_wheel_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shehsin',
    maintainer_email='mohammedshehsin654@email.com',
    description='4-Wheel URDF Robot Simulation with ROS 2',
    license='MIT',
    tests_require=['pytest'],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
    ],
    entry_points={
        'console_scripts': [],
    },
)

