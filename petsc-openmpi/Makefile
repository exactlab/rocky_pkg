# petsc-openmpi RPM Build Makefile

# .PHONY: build clean setup prepare spec-only interactive image
.PHONY: interactive image link nuke

clean:
	rm -rf /home/builder/rpmbuild/

unpack:
	rpm -ivh /home/builder/artifacts/*.src.rpm
	cp /home/builder/artifacts/*.spec /home/builder/rpmbuild/SPECS

build: unpack
	rpmbuild -bb rpmbuild/SPECS/petsc.spec

# Run interactive container from host (run from host directory)
interactive:
	podman run -it --rm \
		-v $(PWD):/home/builder/artifacts:Z,rw \
		rocky-pkg-petsc-openmpi

image:
	podman build -f Containerfile.petsc-openmpi -t rocky-pkg-petsc-openmpi .

source:
	curl -O "https://dl.fedoraproject.org/pub/epel/9/Everything/source/tree/Packages/p/petsc-3.20.6-4.el9.src.rpm"

copy-rpms:
	mkdir -p RPMS
	podman cp $(shell podman ps -q --filter "ancestor=rocky-pkg-petsc-openmpi"):/home/builder/rpmbuild/RPMS/x86_64/. RPMS/
