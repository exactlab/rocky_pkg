# PNetCDF RPM Build Makefile

.PHONY: build clean setup prepare spec-only interactive image

# Default target: build the RPM
build: setup prepare
	rpmbuild -ba --define "_topdir $(HOME)/build" ~/build/SPECS/pnetcdf.spec

# Build only RPMs from existing build tree (fast for spec changes)
spec-only: setup
	ln -sf ~/workspace/pnetcdf.spec ~/build/SPECS/
	rpmbuild -bb --short-circuit --define "_topdir $(HOME)/build" ~/build/SPECS/pnetcdf.spec

# Setup rpmbuild directories
setup:
	mkdir -p ~/build/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

# Prepare sources and spec
prepare: setup
	ln -sf ~/workspace/pnetcdf.spec ~/build/SPECS/
	ln -sf ~/pnetcdf-1.12.3.tar.gz ~/build/SOURCES/

# Clean build artifacts
clean:
	rm -rf ~/build

# Clean only RPMs (keep build tree)
clean-rpms:
	rm -rf ~/build/RPMS/* ~/build/SRPMS/*

# Copy built RPMs to output volume
install:
	mkdir -p ~/rpms
	cp ~/build/RPMS/x86_64/*.rpm ~/rpms/ 2>/dev/null || true
	cp ~/build/SRPMS/*.rpm ~/rpms/ 2>/dev/null || true
	ls -la ~/rpms/
	@echo "RPMs copied to ~/rpms/ - copy them manually from host with:"
	@echo "podman cp \$$(podman ps -lq):/home/builder/rpms/ ."

# Install runtime dependencies
install-deps:
	sudo dnf install -y openmpi netcdf-openmpi hdf5-openmpi

# Test install the built RPMs
test-install: install install-deps
	@echo "Checking available OpenMPI libraries:"
	find /usr/lib64/openmpi/lib -name "libmpi*.so*" 2>/dev/null || true
	sudo dnf install -y ~/rpms/pnetcdf-1.12.3-1.el9.x86_64.rpm ~/rpms/pnetcdf-devel-1.12.3-1.el9.x86_64.rpm --skip-broken

# Run interactive container from host (run from host directory)
interactive:
	podman run -it --rm \
		-v $(PWD):/home/builder/workspace:Z,rw \
		rocky-pkg-pnetcdf

image:
	podman build -f Containerfile.pnetcdf -t rocky-pkg-pnetcdf .
