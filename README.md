# Four-Wheel-Bot-ROS2 🤖

A simple mobile robot model with four wheels designed using **ROS 2** and **Gazebo simulation**. This project demonstrates URDF modeling, TF broadcasting, and integration with `robot_state_publisher` to simulate basic robot structure and movement.

---

## 📦 Project Structure

```
four_wheel_bot/
├── urdf/
│   └── robot.urdf.xacro
├── launch/
│   └── display.launch.py
├── package.xml
└── setup.py
```

---

## 🚀 Features

- Robot model defined using `xacro` (XML macros for URDF)
- Spawns in **Gazebo** simulation
- Visualizes robot and TFs in **RViz2**
- Modular design: you can extend with sensors or controllers later

---

## 🛠️ Dependencies

- ROS 2 (Humble or later)
- `gazebo_ros`
- `xacro`
- `robot_state_publisher`
- `joint_state_publisher`

---

## 🧪 How to Run

### 1. Build the workspace

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### 2. Launch robot in RViz

```bash
ros2 launch four_wheel_bot display.launch.py
```

### 3. Spawn in Gazebo

In another terminal:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch gazebo_ros gazebo.launch.py
ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity four_wheel_bot
```

---

## 📌 Notes

- Make sure `robot_state_publisher` is running and the `robot_description` topic is published properly.
- If the robot is not visible in **RViz** or **Gazebo**, check:
  - `base_link` is set as **Fixed Frame**
  - Zoom out in the 3D view
  - Visual elements are correctly defined in the URDF
- The robot is scaled reasonably to real-world sizes. Adjust the size in `robot.urdf.xacro` if needed.

---

## 🧑‍💻 Author

**Mohammed Shehsin**  
GitHub: [Mohammed-Shehsin](https://github.com/Mohammed-Shehsin)

---

## 📝 License

This project is licensed under the **MIT License**.
