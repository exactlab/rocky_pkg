# PNetCDF Package Builder

Build Rocky Linux RPM packages for parallel-netcdf from upstream sources.

## Build the Image

```bash
cd pnetcdf
podman build -f Containerfile.pnetcdf -t rocky-pkg-pnetcdf .
```

## Build the RPM

Run container interactively:
```bash
make interactive
```

Or manually:
```bash
mkdir -p output build
podman run -it --rm \
  --user $(id -u):$(id -g) \
  -v ./output:/home/builder/output:Z \
  -v ./build:/home/builder/rpmbuild:Z \
  -v .:/home/builder/sources:Z \
  rocky-pkg-pnetcdf
```

Inside the container:
```bash
make build
make install
```

## Available Makefile Targets

### Host targets (run from host):
- `make interactive` - Start container with all volumes mounted

### Container targets (run inside container):
- `make build` - Full build: extract, compile, and package RPMs
- `make spec-only` - Fast rebuild for spec file changes (skips compilation)
- `make prepare` - Setup rpmbuild environment and copy sources
- `make clean` - Clean all build artifacts
- `make clean-rpms` - Clean only RPMs (keep build tree for caching)
- `make install` - Copy built RPMs to output volume

## Fast Iteration

For spec file changes after initial build:
```bash
make spec-only
make install
```

## Files

- `pnetcdf.spec` - RPM spec file for building package
- `Makefile` - Build automation
- `Containerfile.pnetcdf` - Container image definition

## Output

Built RPM packages will be available in the `./output/` directory on the host.