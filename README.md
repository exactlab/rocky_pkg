# Rocky Linux Package Builder

Containerized environment template for building Rocky Linux 9 RPM packages from
source code. This project provides a reusable template for packaging any source
distribution.

## Project Structure

Sources are packaged in subdirectories.

```
rocky_pkg/
├── Containerfile          # Base Rocky Linux 9 build environment
├── <package_name>/
│   ├── Containerfile.<package_name>  # Package-specific dependencies
│   ├── Makefile           # Build automation
│   ├── <package_name>.spec  # RPM spec file
│   └── <source_tarball>   # Source distribution
```

## Creating a New Package

### 1. Prepare Package Directory

Create a directory for your package. You may use the files used to package
`pnetcdf` as a template:

```bash
mkdir <package_name>
cp pnetcdf/Makefile <package_name>/
cp pnetcdf/Containerfile.pnetcdf <package_name>/Containerfile.<package_name>
```

### 2. Build Process

1. **Build the base image:**
```bash
podman build -t rocky-pkg-builder .
```

2. **Build package-specific image:**
```bash
cd <package_name>
make image PACKAGE_NAME=<package_name>
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

### 3. Required Customizations

#### Containerfile.<package_name>
- Update package dependencies
- Install build tools specific to your package
- Configure environment variables

#### <package_name>.spec
- Create RPM spec file defining build process
- Set dependencies, file lists, and metadata
- Configure post-install scripts if needed

#### Makefile
- Update source download URLs
- Modify build targets as needed

### Installation

Install built RPMs:
```bash
sudo dnf install <package_name>/RPMS/<package_name>-*.rpm
```

## Container Architecture

- **Base image**: Rocky Linux 9 with development tools
- **Builder user**: Non-privileged build environment
- **Volume mounting**: Host directory mounted as `/home/builder/artifacts`
- **Artifact extraction**: RPMs copied to host via `make copy-rpms`

## Example: PNetCDF Package

The `pnetcdf/` directory serves as a complete example implementation
demonstrating:
- MPI library integration (OpenMPI 4.1.1)
- Environment module configuration
- Fortran and C++ bindings
- Complex dependency management

## Built Packages

This project builds the following RPM packages:

- **pnetcdf/**
  - `pnetcdf`
  - `pnetcdf-devel`
- **petsc-openmpi/**
  - `petsc`
  - `petsc-devel`
  - `petsc-doc`
  - `petsc-openmpi`
  - `petsc-openmpi-devel`

## Requirements

- Podman or Docker
- Rocky Linux 9 host (recommended)
