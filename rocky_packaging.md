# Rocky Linux Packaging Guide

## Overview
Rocky Linux packaging involves building RPM packages from source, primarily
for maintaining packages compatible with Rocky Linux 9 and above.

## Prerequisites

### System Requirements
- Rocky Linux or compatible RPM-based system
- Basic development tools

### Dependencies
```bash
dnf install git make golang
```

## Rocky Devtools Setup

### Download and Install
```bash
# Download Rocky Devtools
curl -OJL https://github.com/rocky-linux/devtools/archive/refs/heads/main.zip

# Extract and install
unzip devtools-main.zip
cd devtools-main
make
sudo make install
```

### Core Tools
- `rockyget`: Download source RPMs and dependencies
- `rockybuild`: Build packages from sources
- `rockypatch`: Apply patches to packages
- `rockyprep`: Prepare build environment

## Packaging Workflow

### 1. Source Acquisition
```bash
# Search and download SRPM for a package
rockyget <package-name>
```
Creates directory structure: `~/rocky/rpms/<package-name>/`

### 2. Package Building
```bash
# Build package from downloaded sources
rockybuild <package-name>
```

### 3. Build Artifacts
- Build logs: `~/rocky/builds/<package-name>/r8/`
- Key logs: `build.log`, `root.log`

## Key Concepts

### SPEC Files
- Central to RPM packaging
- Defines build process, dependencies, installation steps
- Located in package source directory
- May require debranding for Rocky Linux compatibility

### Chroot Environment
- Isolated build environment
- Ensures consistent, reproducible builds
- Managed by `rockybuild`

## Debugging Build Issues

### Log Analysis
1. Check `~/rocky/builds/<package-name>/r8/build.log` for build errors
2. Review `~/rocky/builds/<package-name>/r8/root.log` for system-level issues
3. Examine SPEC file for potential modifications needed

### Common Issues
- Missing build dependencies
- Upstream source incompatibilities
- Branding elements requiring modification

## Best Practices

### Development Workflow
1. Always use clean chroot environments
2. Review SPEC files for Rocky Linux compatibility
3. Test builds thoroughly before submission
4. Document any custom patches or modifications

### Package Maintenance
- Track upstream changes
- Maintain compatibility with Enterprise Linux standards
- Follow Rocky Linux branding guidelines
- Keep build dependencies minimal and well-defined