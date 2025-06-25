# Use an official TeX Live image as the base image
FROM texlive/texlive:latest

# Install necessary tools, including SSH client and Git
RUN apt-get update && apt-get install -y \
    openssh-client \
    git \
    bash \
    && apt-get clean

# Set up a non-root user for development
ARG USERNAME=vscode
ARG USER_UID=1001
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get install -y sudo \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Switch to the development user
USER $USERNAME

# Run bash as the default shell
CMD ["bash"]