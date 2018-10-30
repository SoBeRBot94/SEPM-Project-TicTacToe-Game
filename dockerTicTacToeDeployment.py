#!/usr/bin/env python3

import pip

pip.main(['install', 'docker'])

import docker
import os

dockerClient = docker.from_env()

dockerClient.images.build(path="./", tag="tictactoe:alpine", rm=True)

runContainer="/usr/bin/docker run --rm --interactive tictactoe:alpine"
os.system(runContainer)
