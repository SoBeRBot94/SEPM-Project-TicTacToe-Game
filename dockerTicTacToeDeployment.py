#!/usr/bin/env python3

import pip

pip.main(['install', 'docker'])

import docker
import os

dockerClient = docker.from_env()

dockerClient.images.build(path="./", tag="tictactoe:test", rm=True)

runContainer="/usr/bin/docker run --rm --interactive tictactoe:test"
os.system(runContainer)
