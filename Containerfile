FROM rockylinux:9

# Install basic development tools and dependencies
RUN dnf update -y
RUN dnf install -y dnf-plugins-core
RUN dnf config-manager --set-enabled crb
RUN dnf install -y epel-release
RUN dnf groupinstall -y "Development Tools"
RUN dnf install -y git make golang rpm-build rpm-devel unzip sudo createrepo_c && \
    dnf clean all

# Create build user and enable sudo
RUN useradd -m -s /bin/bash builder && \
    usermod -aG wheel builder && \
    echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Switch to builder user
USER builder
WORKDIR /home/builder

# Download and install Rocky Devtools
RUN curl -OJL https://github.com/rocky-linux/devtools/archive/refs/heads/main.zip
RUN unzip devtools-main.zip
WORKDIR /home/builder/devtools-main
RUN go mod init rocky-devtools
RUN make
RUN touch .dnf .system
RUN sudo mkdir -p /usr/share/nginx/html/repo
RUN sudo make install

# Create directories for build artifacts
RUN mkdir -p /home/builder/rocky/rpms /home/builder/rocky/builds
RUN chown -R builder:builder /home/builder/rocky

# Switch back to builder user
USER builder
WORKDIR /home/builder

# Set up environment
ENV HOME=/home/builder
ENV USER=builder

CMD ["/bin/bash"]
