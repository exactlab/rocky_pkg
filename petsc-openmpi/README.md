# PETSc OpenMPI Package Rebuild

This directory contains a rebuild of the PETSc packages with modifications for
compatibility and scope reduction.

This rebuild produces only the essential OpenMPI PETSc packages:
- `petsc-openmpi` - OpenMPI parallel version
- `petsc-openmpi-devel` - Development files for OpenMPI version
- `petsc` - Serial version (dependency)
- `petsc-devel` - Serial development files (dependency)
- `petsc-doc` - Documentation and license files


## Changes from Upstream

### 1. OpenMPI Epoch Fix
The original package required `openmpi-devel 1:4.1.1` but available version is
`2:4.1.1` (epoch mismatch)
**Changes**:
- **File**: `petsc.spec`
  - Updated epoch from `1` to `2` in spec file (line 39)

### 2. Package Scope Reduction
Only the following packages are rebuilt:
- `petsc` (serial version)
- `petsc-devel`
- `petsc-openmpi`
- `petsc-openmpi-devel`
- `petsc-doc` (for license compliance)

**Changes**:
- **File**: `petsc.spec`
  - `%bcond_with mpich` - disabled MPICH variant
  - `%bcond_with arch64` - disabled 64-bit integer variant
  - `%bcond_with python` - disabled Python bindings
  - Removed corresponding `%package` and `%files` sections

### 3. Test Disabling
To speed up the build process.
**Changes**:
- **File**: `petsc.spec`
  - Changed `%bcond_without check` to `%bcond_with check`

## Rebuild:
```bash
make source  # fetch source rpm package
make image   # build build-environment container image
make interactive  # start the container and enter into it
# Now in the container
make build
# Back in the host, **without closing the interactive session**
make copy  # copy RPMs from container to host.
```
