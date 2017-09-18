#!/usr/bin/env bash
echo -e "Building The TicTacToe Vagrant Machine \n PLEASE WAIT ..."

# Variables
user=/home/vagrant
git_repo_url=https://github.com/SoBeRBot94/TicTacToe-GE.git
vs_code_url=https://az764295.vo.msecnd.net/insider/b0c0634339c6f64a5c7f08b56fe732fb9154d3c4/code-insiders_1.17.0-1505452681_amd64.deb

# Install Requirements

# Python 3.6

Install_py () {
	sudo add-apt-repository ppa:jonathonf/python-3.6 -y
	sudo apt-get update -y
	sudo apt-get install python3.6 -y
	sudo apt-get install ipython ipython3 -y
	sudo apt-get install python-virtualenv -y
	pip install ipython
}

Install_py

# Git

Install_requirements () {
	# Git
	sudo apt-get install git -y

	# Atom
	sudo add-apt-repository ppa:webupd8team/atom -y
	sudo apt-get update -y
	sudo apt-get install atom -y

	# Sublime Text
	sudo add-apt-repository ppa:webupd8team/sublime-text-3 -y
	sudo apt-get update -y
	sudo apt-get install sublime-text-installer -y

	# Visual Studio Code
	mkdir /home/vagrant/temp
	wget --output-document=$user/temp/visual-studio-code.deb $vs_code_url
	sudo dpkg -i $user/temp/visual-studio-code.deb
}

Install_requirements

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

# Set Permissions & Owner

Set_permissions_owner () {
	sudo chown -R vagrant:vagrant $user/TicTacToe
}

Set_permissions_owner

# Return Versions

Return_ver () {
	python_version=$(python3.6 --version)
	git_version=$(git --version)

	echo $python_version
	echo $git_version
}

Return_ver

echo -e "Build Complete"
