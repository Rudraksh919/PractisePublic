FROM dustynv/ros:foxy-ros-base-l4t-r32.7.1

# Copy the ZED SDK installer
COPY ZED_SDK_Tegra_L4T32.6_v3.8.2.zstd.run /tmp/ZED_SDK.run

# Install dependencies and ZED SDK
RUN apt-get update && apt-get install -y \
    lsb-release \
    libusb-1.0-0 \
    libqt5gui5 \
    libqt5core5a \
    libqt5widgets5 \
    libgl1-mesa-glx \
    libegl1-mesa \
    && chmod +x /tmp/ZED_SDK.run && \
    /tmp/ZED_SDK.run -- silent && \
    rm /tmp/ZED_SDK.run

# Source ROS 2
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc