FROM ros:noetic-ros-base

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-rosdep \
    python3-rosinstall \
    python3-rosinstall-generator \
    python3-wstool \
    git \
    build-essential \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN rosdep init || true
RUN rosdep update || true

RUN mkdir -p /root/catkin_ws/src
WORKDIR /root/catkin_ws

RUN /bin/bash -lc "source /opt/ros/noetic/setup.bash && catkin_make || true"

RUN echo "source /opt/ros/noetic/setup.bash" >> /root/.bashrc
RUN echo "source /root/catkin_ws/devel/setup.bash 2>/dev/null || true" >> /root/.bashrc

CMD ["bash"]
