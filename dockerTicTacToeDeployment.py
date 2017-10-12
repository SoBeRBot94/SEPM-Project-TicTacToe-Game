#!/usr/bin/env python3

import pip

pip.main(['install', 'docker'])

import docker
import os

dockerClient = docker.from_env()

dockerClient.images.build(path="./", tag="tictactoe:final", rm=True)

runContainer="/usr/bin/docker run --rm --interactive tictactoe:final"
os.system(runContainer)
