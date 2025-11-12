# Rocky Linux Package Builder

Base container image for building Rocky Linux packages using Rocky Devtools.

## Usage

### 1. Build the base image
```bash
podman build -t rocky-pkg-builder .
```

### 2. Create package-specific image
Create a Containerfile for each package to install its dependencies:
```dockerfile
FROM rocky-pkg-builder
RUN rockyget <package-name>
# Install package-specific build dependencies here
```

Build the package-specific image:
```bash
podman build -f Containerfile.<package-name> -t rocky-pkg-<package-name> .
```

### 3. Run container with volumes
```bash
podman run -it --rm \
  -v ./sources:/home/builder/sources:Z \
  -v ./output:/home/builder/output:Z \
  rocky-pkg-<package-name>
```

This allows you to:
- Modify source code in `./sources/`
- Access build artifacts in `./output/`
- Iterate on builds without rebuilding the container
- Debug and tweak setup easily

## Container Features

- Rocky Linux 9 base
- Rocky Devtools pre-installed
- Non-root `builder` user
- Development tools and RPM build environment
- Ready for volume mounting

## Build Environment

- Working directory: `/home/builder`
- Build logs: `~/rocky/builds/<package>/r8/`
- Source RPMs: `~/rocky/rpms/<package>/`