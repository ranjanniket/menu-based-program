import os

while True:
	os.system('clear')
	os.system(' figlet -f standard -c Docker | lolcat')

	print('''\033[37mSelect your choice, from the menu below:
\033[36m1 Setup docker in rhel 8
\033[36m2 Check docker engine information
\033[36m3 Check docker version
\033[36m4 Select for docker daemon(start/stop/status)
\033[36m5 Select for containers operations
\033[36m6 Select for image operations
\033[36m0 Return to menu
\033[91m99 Exit From The Software
		\033[97m''')

	ch = int(input("Enter your Choice: "))

	if ch == 1:
		os.system('clear')
		os.system('''echo  "[docker1]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0" >> /etc/yum.repos.d/ry.repo ''')
		os.system('yum install docker-ce --nobest')
		os.system('systemctl start docker')
	elif ch == 2:
		os.system('clear')
		os.system('figlet "Docker info"')
		os.system('docker info | less')
		input('Press enter to continue')
	elif ch == 3:
		os.system('clear')
		os.system('figlet "Docker info"')
		os.system('docker version | less')
		input('Press enter to continue')

	elif ch == 4:
		while True:

			os.system('clear')
			os.system('figlet Docker Daemon')
			print('''1 status docker daemon
2 start docker daemon
3 enable docker daemon
4 stop docker daemon
5 disable docker daemon
0 To main menu''')
			ch4 = int(input('Enter choice for docker daemon: '))
			if ch4 == 1:
				os.system('clear')
				os.system('figlet "Docker Status"')
				os.system('systemctl status docker')
				input('Press enter to continue')
			elif ch4 == 2:
				os.system('systemctl enable docker')
			elif ch4 == 3:
				os.system('systemctl stop docker')
			elif ch4 == 4:
				os.system('systemctl disable docker')
			elif ch4 == 0:
				break
			else:
				input('Wrong choice, Press enter to try again')

	elif ch == 5:
		while True:
			os.system('clear')
			os.system('figlet Docker Containers')
			print('''1 Display running containers
2 Display all containers(running+stoped)
3 Launch a container.
4 Start a stopped container.
5 Attach running container to shell.
6 Delete a container.
7 Delete all container.
8 Exec a command in container
9 Copy files in/from container
0 Return to docker menu''')
			ch5 = int(input('Enter choice for, container operation: '))
			if ch5 == 1:
				os.system('docker ps | less')
				input('Press enter to continue')
			elif ch5 == 2:
				os.system('docker ps -a | less')
				input('Press enter to continue')
			elif ch5 == 3:
				os.system('docker ps')
				con_name = input('Enter container name(not already used): ')
				os.system('docker image ls')
				con_image = input(
					'Enter image to be used, from the locally available images: ')
				os.system('docker run -it --name {0} {1}'.format(con_name, con_image))
			elif ch5 == 4:
				os.system('docker ps -a')
				con_name = input('Enter container name or id: ')
				os.system('docker start {}'.format(con_name))
			elif ch5 == 5:
				os.system('docker ps')
				con_name = input('Enter name of running container from above: ')
				os.system('docker attach {}'.format(con_name))
			elif ch5 == 6:
				os.system('docker ps -a')
				con_name_id = input('Enter container name or id: ')
				os.system('docker rm -f {}'.format(con_name_id))
			elif ch5 == 7:
				 os.system('docker rm -f $(docker ps -qa)')
			elif ch5 == 8:
				os.system('docker ps')
				con_name = input('Select & enter container name or id, to be used: ')
				cmd = input('Enter command to be execute on container: ')
				os.system('docker exec {0} {1}'.format(con_name, cmd))
			elif ch5 == 9:
				file_name = input(
					'Enter the file path to be transfered:(Give absolute path) ')
				con_name = input(
					'Enter container name/id, where you need to transfer file: ')
				con_loc = input(
					'Enter location in continer to be transferd:(Give absolute path) ')
				os.system('docker cp {0} {1}:{2}'.format(file_name, con_name, con_loc))
			elif ch5 == 0:
				break
			else:
				input('Wrong choice, Press enter to try again')
	elif ch == 6:
		while True:
			os.system('clear')
			os.system('figlet Docker Images')
			print('''1 List available image in the system.
2 Search image fron shell, with keyword
3 Pull a image from docker hub.
4 Remove a local image.
0 Return to docker menu ''')
			ch6 = int(input('Enter your choice, for Docker image operations: '))
			if ch6 == 1:
				os.system('docker image ls | less')
				input('Press Enter to continue')
			elif ch6 == 2:
				image_keyword = input("Enter keyword to search for image")
				os.system('docker search {}'.format(image_keyword))
				input('Press Enter to continue')
			elif ch6 == 3:
				image_name = input(
					'Enter image name(with tag if required):(use format - <IMAGE NAME>:<TAG>')
				os.system('docker pull {}'.format(image_name))
			elif ch6 == 4:
				os.system('docker image ls')
				image_name = input(
					'Enter image name(with tag if required):(use format - <IMAGE NAME>:<TAG>')
				os.system('docker image rm {}'.format(image_name))
			elif ch6 == 0:
				break
			else:
				input('Wrong choice, Press enter to try again')

	elif ch == 0:
		os.system("python3 menu.py")
	elif ch == 99:
		exit()

	else:
		input('Wrong Choice, Press enter to try again')
