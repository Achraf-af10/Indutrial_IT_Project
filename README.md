# ROS Noetic - Environnement Docker Unifié

## Installation

### Build
docker-compose build

### Lancement
docker-compose up -d

### Accès au conteneur
docker exec -it ros_noetic bash

### Compilation Catkin
cd /root/catkin_ws
catkin_make
source devel/setup.bash

