# BSC thises 

# NDT & ICP lidar matching methods compare and prediction 

# install carla 

# install carla-ros bridge 

# config lidar 

we need to open /carla_ros_bridge/catkin_ws/carla_spawn_objects/config/object.json

then find lidar raycast sensor and change config like velodyne 128 
akse data sheet inja bashe

config 
   "spawn_point": {"x": 0.0, "y": 0.0, "z": 2.4, "roll": 0.0, "pitch": 0.0, "yaw": 0.0},
                    "range": 245,
                    "channels": 128,
                    "points_per_second": 2400000,
                    "upper_fov": 15.0,
                    "lower_fov": -20.0,
                    "rotation_frequency": 20,
                    "noise_stddev": 0.0
                    