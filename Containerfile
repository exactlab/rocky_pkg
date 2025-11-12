# rocky-pkg-builder
FROM rockylinux:9

# Install basic development tools and dependencies
RUN dnf update -y
RUN dnf install -y dnf-plugins-core
RUN dnf config-manager --set-enabled crb && dnf makecache
RUN dnf install -y epel-release
RUN dnf install -y \
    rpm-build rpmdevtools tar && \
    dnf clean all

# Create build user and enable sudo
RUN useradd -m -s /bin/bash builder && \
    usermod -aG wheel builder && \
    echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Switch to builder user
USER builder
WORKDIR /home/builder

# Switch back to builder user
USER builder
WORKDIR /home/builder

# Set up environment
ENV HOME=/home/builder
ENV USER=builder

RUN rpmdev-setuptree

CMD ["/bin/bash"]
