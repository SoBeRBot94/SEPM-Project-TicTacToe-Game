#!/usr/bin/env bash
echo -e "Building The TicTacToe Vagrant Machine \n PLEASE WAIT ..."

# Variables
user=/home/vagrant
git_repo_url=https://github.com/SoBeRBot94/TicTacToe-GE.git

# Install Requirements

# Python 3.6

Install_py () {
	sudo add-apt-repository ppa:jonathonf/python-3.6 -y
	sudo apt-get update -y
	sudo apt-get install python3.6 -y
}

Install_py

# Git

Install_git () {
	sudo apt-get install git -y
}

Install_git

# Setup The Build Environmnet

Setup_build_env () {
	mkdir -p $user/TicTacToe
}

Setup_build_env

# Clone The Git Repo

Clone_git_repo () {
	git clone $git_repo_url $user/TicTacToe
}

Clone_git_repo

# Return Versions

Return_ver () {
	python_version=$(python3.6 --version)
	git_version=$(git --version)

	echo $python_version
	echo $git_version
}

Return_ver

echo -e "Build Complete"
