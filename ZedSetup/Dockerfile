FROM nvcr.io/nvidia/l4t-base:r32.7.1

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    libusb-1.0-0 \
    libgl1-mesa-glx \
    libegl1-mesa \
    libx11-6 \
    libxi6 \
    libxrandr2 \
    libxinerama1 \
    libxcursor1 \
    libglu1-mesa \
    wget \
    unzip \
    && apt-get clean

# Copy ZED SDK installer into the container
COPY ZED_SDK_Tegra_L4T32.6_v3.8.2.zstd.run /tmp/ZED_SDK.run
RUN chmod +x /tmp/ZED_SDK.run

# Install ZED SDK
RUN /tmp/ZED_SDK.run -- silent

# Clean up
RUN rm /tmp/ZED_SDK.run

# Add ZED environment variables
ENV ZED_SDK_ROOT="/usr/local/zed"
ENV LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/zed/lib"

# Set working directory
WORKDIR /workspace

CMD ["/bin/bash"]