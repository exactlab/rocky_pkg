.PHONY: image

image:
	podman build -f Containerfile -t rocky-pkg-builder

default: image
