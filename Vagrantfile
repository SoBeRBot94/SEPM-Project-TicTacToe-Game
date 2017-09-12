# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

# Base Image From Vagrant Cloud
	config.vm.box = "ubuntu/trusty64"

# Define Vagrant Machine
	config.vm.define :TicTacToe do |t|
	end

# Hypervisor Configuration & Virtual Machine Configuration
	config.vm.provider "virtualbox" do |vb|

		# Virtual Machine Name
		vb.name = "TicTacToe-SEPM"

		# Virtual Machine Memory Config
		vb.memory = "1024"
	end

# Vagrant Machine Provision Configuration

	# Bootstrapping Provisioning Using Shell Script
	config.vm.provision "shell", path: "Provision.sh"
end
