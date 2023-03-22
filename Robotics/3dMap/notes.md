# 3d mapping

## Steps

1. ros/rviz point cloud && 
  - Robotic location (offset from first cloud)
    - Is it included in the point cloud?
  - Do I also need rotation info?
2. Python point cloud
  - Adjust(ed) for offset and rotation
3. Python 3d point list
  - Keep and update a global/master 3d point list
  - https://github.com/ros2/common_interfaces/blob/master/sensor_msgs_py/sensor_msgs_py/point_cloud2.py#L157
4. Probalistic test to see if point is actually there
5. Reformat list into cloud that is compatible with RVIZ
  - Maybe: https://docs.m2stud.io/cs/ros_additional/06-L3-rviz/


## Other links

- General rviz info: https://www.youtube.com/watch?v=yLwr5Zhr_t8
- Proof that it can be done: https://www.youtube.com/watch?v=dfKiFW3SGEs
- ros library that "can be used to generate a 3D point clouds of the environment and/or to create a 2D occupancy grid map for navigation"
  - http://wiki.ros.org/rtabmap_ros
