# TicTacToe-GE
---
A TicTacToe Game Engine Wirtten In Python

## Vagrant Development Environment

### Requirements

* Git

* Vagrant

* Any Hypervisor ( Virtualbox Preffered )

---
### Build The Development Environment

* Clone The Repo

```bash
	git clone https://github.com/SoBeRBot94/TicTacToe-GE.git
```

* Build Vagrant Machine

```bash
	cd TicTacToe-GE
	vagrant up
```

** The Vagrant Machine Will Be Provisioned By The Script Named Provision.sh **

* SSH Into The Vagrant Machine

```bash
	vagrant ssh
```

* Find The Repo

```bash
	cd /home/vagrant/TicTacToe/TicTacToe-GE
```

** Develop Here **

* Remove The Devel Vagrant Machine

```bash
	vagrant destroy
```

** Note: This Will Remove The Vagrant Machine & All The Files Associated With It **
