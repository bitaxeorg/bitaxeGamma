.PHONY: bom clean docker_run build-pcb output/version.txt board_render.png board_render_purple.png

GIT_VERSION := $(shell git describe --tags --always)
PYTHON := python3
OUTPUT_DIR := output
OUTPUT_FILE := $(OUTPUT_DIR)/bitaxeGamma-$(GIT_VERSION).zip
LOGFILE?=$(OUTPUT_DIR)/kibot_error.log
DOCKER_IMAGE := registry.gitlab.com/nlighten-systems/kicad_ci:kicad_ci

all: build-pcb

clean:
	rm -rf output

docker_run:
	docker run --rm -it -u "$(shell id -u):$(shell id -g)" -v "$(abspath .):/data" ${DOCKER_IMAGE} /bin/bash

output:
	mkdir -p output

output/version.txt: | output
	echo "$(GIT_VERSION)" > $@

build-pcb: output/version.txt
	kibot -d output -c kibot.yaml -e bitaxeGamma.kicad_sch

