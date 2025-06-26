# 🚗 Four-Wheel Bot – ROS 2 + Gazebo Simulation

This project simulates a four-wheeled mobile robot using ROS 2 (Humble) and Gazebo 11. It includes a URDF model, launch files, and a reliable launch method using two terminals.

---

## 📂 Repository Structure

```
four_wheel_bot/
├── launch/
│   ├── spawn_robot.launch.py
│   └── sim_headless.launch.py
├── urdf/
│   └── four_wheel_bot.urdf.xacro
├── CMakeLists.txt
├── package.xml
└── README.md
```

---

## ✅ Working Launch Method (Recommended)

### 🖥️ Terminal 1: Start Gazebo in headless mode

```bash
gazebo --verbose -s libgazebo_ros_factory.so --headless-rendering
```

### 🖥️ Terminal 2: Build and spawn robot

```bash
cd ~/ros2_ws
rm -rf build install log  # optional cleanup
colcon build
source install/setup.bash
ros2 launch four_wheel_bot spawn_robot.launch.py
```

✔️ This reliably spawns the robot in Gazebo.

---

## 📦 Dependencies

Make sure these packages are installed:

```bash
sudo apt update
sudo apt install ros-humble-gazebo-ros-pkgs ros-humble-gazebo-ros2-control ros-humble-gazebo-plugins
```

---

## 🛠️ Troubleshooting

- **Gazebo closes or crashes instantly**:
  ```bash
  pkill -9 gzserver
  pkill -9 gzclient
  ```

- **Robot doesn’t appear in Gazebo**:
  - Always use the correct plugin:
    ```bash
    gazebo --verbose -s libgazebo_ros_factory.so --headless-rendering
    ```

---

## 🧾 Using This GitHub Repository

To use this repository:

```bash
cd ~/ros2_ws/src
git clone https://github.com/Mohammed-Shehsin/Four-Wheel-Bot-ROS2.git four_wheel_bot
cd ~/ros2_ws
colcon build
source install/setup.bash
```

Then follow the launch method above.

---

## 📄 Additional Launch Option

You can also run the secondary launch file:

```bash
ros2 launch four_wheel_bot sim_headless.launch.py
```

Make sure the following dependencies exist in `package.xml`:

```xml
<exec_depend>launch</exec_depend>
<exec_depend>launch_ros</exec_depend>
```

---

## 👤 Author

**Mohammed Shehsin**  
[GitHub – Mohammed-Shehsin](https://github.com/Mohammed-Shehsin)  
📧 mohamedshehsin@gmail.com

---

## 📜 License

This project is licensed under the MIT License.
