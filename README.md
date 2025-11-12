# Rocky Linux Package Builder

Containerized environment for building Rocky Linux 9 RPM packages with support for MPI-enabled packages like PNetCDF.

## Project Structure

```
rocky_pkg/
├── Containerfile          # Base Rocky Linux 9 build environment
├── pnetcdf/
│   ├── Containerfile.pnetcdf  # PNetCDF-specific dependencies
│   ├── Makefile           # Build automation
│   ├── pnetcdf.spec       # RPM spec file
│   └── pnetcdf-1.12.3.tar.gz # Source tarball
```

## PNetCDF Package

### Build Process

1. **Build the base image:**
```bash
podman build -t rocky-pkg-builder .
```

2. **Build PNetCDF-specific image:**
```bash
cd pnetcdf
make image
```

3. **Download source (if needed):**
```bash
make source
```

4. **Run interactive container:**
```bash
make interactive
```

5. **Build RPM (inside container):**
```bash
make build
```

6. **Copy RPMs to host:**
```bash
make copy-rpms
```

### Features

- OpenMPI 4.1.1 integration with environment modules
- Automatic MPI library dependency handling
- Fortran and C++ bindings support
- Rocky Linux 9 compatibility

### Installation

The built RPMs include post-install scripts to configure MPI library paths:
```bash
sudo dnf install pnetcdf/RPMS/pnetcdf-*.rpm
```

## Container Architecture

- **Base image**: Rocky Linux 9 with development tools
- **Builder user**: Non-privileged build environment
- **Volume mounting**: Host directory mounted as `/home/builder/artifacts`
- **Artifact extraction**: RPMs copied to host via `make copy-rpms`

## Requirements

- Podman or Docker
- Rocky Linux 9 host (recommended)
- OpenMPI runtime for package installation