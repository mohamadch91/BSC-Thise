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

1. Setup your sources.list

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
2. Set up your keys

```bash

sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
3. Installation

```bash
sudo apt update
sudo apt install ros-noetic-desktop-full
```
4. Environment setup

```bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
5. Dependencies for building packages

```bash
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```
6. Initialize rosdep

```bash
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
```
done 

you can see more info in [this link](http://wiki.ros.org/noetic/Installation/Ubuntu)


#### install carla-ros bridge 

we use source Repository for install carla-ros bridge

1. Create a catkin workspace

```bash
 mkdir -p ~/carla-ros-bridge/catkin_ws/src
```
2. Clone the repository into the src folder

```bash
    cd ~/carla-ros-bridge
    git clone --recurse-submodules https://github.com/carla-simulator/ros-bridge.git catkin_ws/src/ros-bridge
   ```
3. set up the environment

```bash
        source /opt/ros/<melodic/noetic>/setup.bash 
```
or you can use this command for set up the environment

```bash
        source ~/.bashrc
```
4. Install dependencies

```bash
        rosdep update
        rosdep install --from-paths src --ignore-src -r 
```
5. Build the package

```bash
        catkin_make
```
##### run carla-ros bridge

1. run carla

```bash
    cd /opt/carla-simulator
    ./CarlaUE4.sh -prefernvidia -quality-level=Low
```

2. Add the correct CARLA modules to your Python path:

```
export CARLA_ROOT=<path-to-carla>
export PYTHONPATH=$PYTHONPATH:$CARLA_ROOT/PythonAPI/carla/dist/carla-<carla_version_and_arch>.egg:$CARLA_ROOT/PythonAPI/carla
```
3. Add source 
```
source ~/carla-ros-bridge/catkin_ws/devel/setup.bash
```
4. run carla-ros bridge

```
roslaunch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch
```

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



