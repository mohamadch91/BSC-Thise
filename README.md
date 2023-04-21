# BSC thises 

# NDT & ICP lidar matching methods compare and prediction 

## Install
### install carla 
we use carla 0.9.11 version quick install guide is here 

installation for ubuntu 20.04


#### check python version
```bash
python --version
# and

pip3 --version
```
if you need to upgrade pip:
```bash
pip3 install --upgrade pip
```
 then we need to install numpy and pygame

```bash
pip3 install numpy pygame
```
#### install carla

1. Set up the Debian repository in the system:

```bash

 sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1AF1527DE64CB8D9
sudo add-apt-repository "deb [arch=amd64] http://dist.carla.org/carla $(lsb_release -sc) main"

```
2. Install CARLA and check for the installation in the /opt/ folder:

```bash

  sudo apt-get update # Update the Debian package index
    sudo apt-get install carla-simulator # Install the latest CARLA version, or update the current installation
    cd /opt/carla-simulator # Open the folder where CARLA is installed
```
3. install client library

```bash
 pip3 install carla
```
4. run carla

```bash
   cd /opt/carla-simulator
 ./CarlaUE4.sh -prefernvidia -quality-level=Low
```

5. run carla client

```bash
 # Terminal A 
        cd PythonAPI\examples

        python3 -m pip install -r requirements.txt # Support for Python2 is provided in the CARLA release packages

        python3 generate_traffic.py  

        # Terminal B
        cd PythonAPI\examples

        python3 manual_control.py 
```
If pygame screen is shown, then everything is ok.

you can see more info in [this link](https://carla.readthedocs.io/en/latest/start_quickstart/)
#### install ros 



### install carla-ros bridge 

### config lidar 

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
                    

## generate point cloud 

we need to run carla first 

then run pointcloud generator from pcl package from  ros-bridge



