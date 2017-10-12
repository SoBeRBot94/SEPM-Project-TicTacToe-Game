# TicTacToe-GE
---
A TicTacToe Game Engine Wirtten In Python

## Vagrant Development Environment

### Requirements

* Git

* Vagrant

* Any Hypervisor ( Virtualbox Preferred )

---
### Build The Development Environment

* Clone The Repo

```bash
	git clone https://github.com/SoBeRBot94/TicTacToe-GE.git
```

* Build Vagrant Machine

```bash
	cd TicTacToe-GE

	vagrant up --provider=virtaulbox
```

**The Vagrant Machine Will Be Provisioned By The Script Named Provision.sh**

* SSH Into The Vagrant Machine

```bash
	vagrant ssh
```

* Find The Repo

```bash
	cd /home/vagrant/TicTacToe/TicTacToe-GE
```

**Develop Here**

* Shutdown The Devel Vagrant Machine

```bash
	vagrant halt
```

* Remove The Devel Vagrant Machine

```bash
	vagrant destroy
```

**Note: This Will Remove The Vagrant Machine & All The Files Associated With It**

---

## Play TicTacToe

### Requirements

* Git

* Docker

### Work With Docker

* Clone The Git Repository

```bash
	git clone https://github.com/SoBeRBot94/TicTacToe-GE.git
```

* Build The Image

```bash
	docker build --rm --tag tictactoe:final ./
```

* Run The Container With STDIN Enabled

```bash
	docker run --rm --interactive tictactoe:final
```

### Bootstrap The Containers Using Python

```bash
	chmod u+x ./dockerTicTacToeDeployment.py
```

```bash
	./dockerTicTacToeDeployment.py
```

**Enjoy Your Game**
