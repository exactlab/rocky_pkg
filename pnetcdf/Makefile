# PNetCDF RPM Build Makefile

# .PHONY: build clean setup prepare spec-only interactive image
.PHONY: interactive image link nuke

nuke:
	rm -rf /home/builder/rpmbuild/
	rpmdev-setuptree

link:
	ln -s /home/builder/artifacts/*.spec rpmbuild/SPECS/ || true
	ln -s /home/builder/artifacts/*.tar.gz rpmbuild/SOURCES/ || true

build: link
	rpmbuild -bb rpmbuild/SPECS/pnetcdf.spec

# Run interactive container from host (run from host directory)
interactive:
	podman run -it --rm \
		-v $(PWD):/home/builder/artifacts:Z,rw \
		rocky-pkg-pnetcdf

image:
	podman build -f Containerfile.pnetcdf -t rocky-pkg-pnetcdf .

source:
	curl -O "https://parallel-netcdf.github.io/Release/pnetcdf-1.12.3.tar.gz"

copy-rpms:
	mkdir -p RPMS
	podman cp $(shell podman ps -q --filter "ancestor=rocky-pkg-pnetcdf"):/home/builder/rpmbuild/RPMS/x86_64/. RPMS/
