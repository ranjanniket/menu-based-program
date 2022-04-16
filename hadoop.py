import os
from platform import system


def hadoop_logo_first():
	if system() == 'Linux':
		os.system("clear")
		os.system("figlet -f standard -c Hadoop | lolcat ")


def hadoop_logo():
	if system() == 'Linux':
		os.system("clear")
		os.system("figlet -f standard -c Hadoop | lolcat ")

c = "Choice == "


def hadoop_list():
	print("""\033[33m
				\033[32mChoose Your Role

		\033[36m[1] Master
		\033[36m[2] Slave
		\033[36m[3] Configure the Required Hadoop Application
		\033[36m[0] Return to Main Menu 
		\033[91m[99] Exit To The Software

	\033[97m """)
	#os.system("echo {} | lolcat -a -d 100".format(c))
	hadoop_list_x = int(input("Choice==>> "))

	if hadoop_list_x == 1:
		master_menu()

	elif hadoop_list_x == 2:
		slave_menu()

	elif hadoop_list_x == 3:
		hadoop_logo()

		print("""\033[33m
			\033[32mChoose where to install JAVA & HADOOP

		\033[36m[1] Local Computer
		\033[36m[2] Throw The SSH local storage software
		\033[36m[3] Throw The SSH and download the Software with Cloud
		\033[36m[4] Test
		\033[36m[5] Return

	\033[97m """)
		configure_x = int(input("Choice==>> "))
		if configure_x == 2:
			#os.system("sudo yum install wget -y")
			#os.system("wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
			#os.system("wget https://mirrors.huaweicloud.com/java/jdk/8u171-b11/jdk-8u171-linux-x64.rpm")
			#os.system("ssh root@{} sudo rpm -i /root/arth/src/app/jdk-8u171-linux-x64.rpm".format())
			#os.system("ssh root@{} sudo rpm -i hadoop-1.2.1-1.x86_64.rpm --force".format())
			connect_throw_ssh()
			hadoop_logo()
			hadoop_list()

		elif configure_x == 1:
			os.system("sudo rpm -i ~/python/src/app/jdk-8u171-linux-x64.rpm")
			os.system("sudo rpm -i ~/python/src/app/hadoop-1.2.1-1.x86_64.rpm --force")
			os.system("echo Success")
			input("Press Enter To Continue: ")
			hadoop_logo()
			hadoop_list()
		elif configure_x == 3:
			connect_throw_ssh_cloud()

		elif configure_x == 4:
			only_test()

		else:
			hadoop_logo()
			hadoop_list()


def master_menu():
	hadoop_logo()
	print("""
			1. Create the Storage Destination
			2. Configure the Hadoop Files
			3. Format the Name Node
			4. Start the Name Node 
			5. Show the Connected Slave
			6. Return to Menu
		""")

	master_menu_x = int(input("Choice ==>>  "))
	master_menu_1(master_menu_x)


def master_menu_1(got_input):
	if got_input == 1:

		x = local_ssh()
		create_directory(x)

	elif got_input == 2:
		hadoop_logo()
		print("""
			1. hdfs-site.xml (LOCAL)
			2. hdfs-site.xml (SSH)
			3. core-site.xml (LOCAL)
			4. core-site.xml (SSH)
		""")
		site_x = int(input("Enter which file want to configure: "))
		file_modification_master(site_x)

	elif got_input == 3:
		x = local_ssh()
		if x == 1:
			os.system("sudo hadoop namenode -format")
			input("Press Enter to Continue: ")
		elif x == 2:
			ip = input("Enter the IP: ")
			os.system("ssh root@{} hadoop namenode -format".format(ip))
			input("Press Enter to Continue: ")

		elif x == 99:
			hadoop_logo()
			hadoop_list()
		else:
			os.sysetm("echo 'Wrong Input Try Again!' | lolcat -a -d 50")

	elif got_input == 4:
		x = local_ssh()
		if x == 1:
			os.system("sudo hadoop-daemon.sh start namenode")
			input("Press Enter to Continue: ")
		elif x == 2:
			ip = input("Enter the IP: ")
			os.system("ssh root@{} sudo hadoop-daemon.sh start namenode")
			input("Press Enter to Continue: ")
		elif x == 99:
			hadoop_logo()
			hadoop_list()
		else:
			os.sysetm("echo 'Wrong Input Try Again!' | lolcat -a -d 50")

	elif got_input == 5:
		x = local_ssh()
		if x == 1:
			os.system("sudo hadoop dfsadmin -report")
			input("Press Enter to Continue: ")
		elif x == 2:
			ip = input("Enter the IP: ")
			os.system("ssh root@{} sudo hadoop dfsadmin -report".format(ip))
			input("Press Enter to Continue: ")
		elif x == 99:
			hadoop_logo()
			hadoop_list()
		else:
			os.sysetm("echo 'Wrong Input Try Again!' | lolcat -a -d 50")

	elif got_input == 6:
		hadoop_logo()
		hadoop_list()


def local_ssh():
	hadoop_logo()
	print("""
1. LOCAL MACHINE
2. OVER THE SSH
99. Exit
		""")
	x = int(input("Choice ==>> "))
	return x


def file_modification_master(input_x):
	if input_x == 1:
		folder_name = input(
			"Enter the same folder name here (eg. dd drive without /) : ")
		os.system("sudo sed 's/namenode/{}/g' ./src/file/hdfs-site.xml | sudo tee /etc/hadoop/hdfs-site.xml".format(folder_name))
		print("Writed")
	elif input_x == 2:
		folder_name = input(
			"Enter the same folder name here (eg. dd drive without /) : ")
		os.system("sudo sed 's/namenode/{}/g' ./src/file/hdfs-site.xml | sudo tee ./src/new/hdfs-site.xml".format(folder_name))
		ip = input("Enter the IP: ")
		os.system("sudo scp ./src/new/* root@{}:/etc/hadoop/ ".format(ip))
		print("Copied")
	elif input_x == 3:
		os.system("sudo cp ./src/file/core-site.xml /etc/hadoop/")
		print("core-site.xml created")
		input("Enter to Continue: ")
	elif input_x == 4:
		ip = input("Enter the IP: ")
		os.system("sudo scp ./src/file/core-site.xml root@{}:/etc/hadoop/".format(ip))
		print("core-site.xml created")
		input("Enter the continue: ")


def file_modification_slave(input_x):
	if input_x == 1:
		folder_name = input(
			"Enter the same folder name here (eg. dd drive without /) : ")
		os.system("sudo sed 's/namenode/{}/g' ./src/file/hdfs-site.xml | sudo tee /etc/hadoop/hdfs-site.xml".format(folder_name))
		print("Writed")
	elif input_x == 2:
		folder_name = input(
			"Enter the same folder name here (eg. dd drive without /) : ")
		os.system("sudo sed 's/namenode/{}/g' ./src/file/hdfs-site.xml | sudo tee ./src/new/hdfs-site.xml".format(folder_name))
		ip = input("Enter the IP: ")
		os.system("sudo scp ./src/new/* root@{}:/etc/hadoop/ ".format(ip))
		print("Copied")
	elif input_x == 3:
		os.system("sudo cp ./src/file/core-site.xml /etc/hadoop/")
		print("core-site.xml created")
		input("Enter to Continue: ")
	elif input_x == 4:
		ip = input("Enter the IP: ")
		os.system("sudo scp ./src/file/core-site.xml root@{}:/etc/hadoop/".format(ip))
		print("core-site.xml created")
		input("Enter the continue: ")


def create_directory(input_y):
	if input_y == 1:
		folder_name = input("Enter the Folder name (example /nn /nd /folder_name) :")
		os.system("sudo mkdir {}".format(folder_name))
		os.system('echo "Folder Created" | lolcat ')
		input("Press Enter to Continue")
		master_menu()
	elif input_y == 2:
		folder_name = input("Enter the Folder name (example /nn /nd /folder_name) :")
		ip = input("Enter the IP: ")
		os.system("ssh root@{} mkdir {}".format(ip, folder_name))

	elif input_y == 99:
		hadoop_logo()
		hadoop_list()

	else:
		os.sysetm("echo 'Wrong Input Try Again!' | lolcat -a -d 50")


def install_java_hadoop():
	ssh_ip = input("Enter the IP Address: ")
	#os.system("ssh root@{} sudo rpm -i /root/arth/src/app/jdk-8u171-linux-x64.rpm".format())
	#os.system("ssh root@{} sudo rpm -i /root/arth/src/app/hadoop-1.2.1-1.x86_64.rpm --force".format())


def connect_throw_ssh():
	ssh_ip = input("Enter the IP Address: ")
	os.system("ssh root@{} mkdir /root/arth /root/arth/src /root/arth/src/app /root/arth/src/file /root/arth/src/new".format(ssh_ip))
	os.system('echo "Folder Created" | lolcat')
	os.system("scp ~/Arth_Team_Task1/*.py root@{}:/root/arth/".format(ssh_ip))
	os.system('echo "File Copied" | lolcat')
	#os.system("scp ~/Arth_Team_Task1/jdk-8u171-linux-x64.rpm ~/Arth_Team_Task1/hadoop-1.2.1-1.x86_64.rpm root@{}:/root/arth/src/app".format(ssh_ip))
	#os.system('echo "Another File Copied" | lolcat')
	input("Press Enter To install this Hadoop: ")
	os.system("ssh root@{} sudo yum install wget -y".format(ssh_ip))
	os.system("ssh root@{} 'wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm -P /root/arth/src/app'".format(ssh_ip))
	os.system("ssh root@{} 'wget https://mirrors.huaweicloud.com/java/jdk/8u171-b11/jdk-8u171-linux-x64.rpm -P /root/arth/src/app'".format(ssh_ip))
	os.system(
		"ssh root@{} sudo rpm -i /root/arth/src/app/jdk-8u171-linux-x64.rpm".format(ssh_ip))
	os.system("ssh root@{} sudo rpm -i /root/arth/src/app/hadoop-1.2.1-1.x86_64.rpm --force".format(ssh_ip))
	input("Press Enter To Continue: ")


def connect_throw_ssh_cloud():
	ssh_ip = input("Enter the IP Address: ")
	os.system("ssh root@{} sudo mkdir /root/arth /root/arth/src /root/arth/src/app /root/arth/src/file /root/arth/src/new".format(ssh_ip))
	os.system('echo "Folder Created" | lolcat')
	os.system("scp ~/Arth_Team_Task1/*.py root@{}:/root/arth/".format(ssh_ip))
	os.system('echo "File Copied" | lolcat')
	os.system("ssh root@{} sudo yum install wget -y".format(ssh_ip))
	os.system("ssh root@{} 'wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm -P /root/arth/src/app'".format(ssh_ip))
	os.system("ssh root@{} 'wget https://mirrors.huaweicloud.com/java/jdk/8u171-b11/jdk-8u171-linux-x64.rpm -P /root/arth/src/app'".format(ssh_ip))
	#os.system("ssh root@{} 'sudo mv hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm /root/arth/src/app'")
	os.system(
		"ssh root@{} 'sudo rpm -i /root/arth/src/app/jdk-8u171-linux-x64.rpm'".format(ssh_ip))
	os.system('echo "JDK INSTALLED" | lolcat')
	os.system("ssh root@{} 'sudo rpm -i /root/arth/src/app/hadoop-1.2.1-1.x86_64.rpm --force'".format(ssh_ip))
	input("Press Enter to Continue: ")


def only_test():
	ssh_ip = input("Enter the IP Address: ")
	os.system(
		"ssh root@{} 'sudo mkdir /root/test; cd /root/test/; touch rahulkumar'".format(ssh_ip))


def input_ip():
	x = input("Entert the Remote IP: ")
	return x


def input_directory():
	x = input("Enter the Name Node Directory to create and Setup: ")
	return x


def slave_menu():
	hadoop_logo()
	print("""
			1. Create the Storage Folder
			2. Configure the Hadoop Files
			3. Start the Data Node
			4. Show the Data Storage
			5. Return to Menu
		""")
	slave_menu_x = int(input("Choice ==>>  "))

	if slave_menu_x == 1:
		x = local_ssh()
		create_directory(x)

	elif slave_menu_x == 2:
		hadoop_logo()
		print("""
			1. hdfs-site.xml (LOCAL)
			2. hdfs-site.xml (SSH)
			3. core-site.xml (LOCAL)
			4. core-site.xml (SSH)
		""")
		site_x = int(input("Enter which file want to configure: "))
		file_modification_slave(site_x)

	elif slave_menu_x == 3:
		x = local_ssh()
		if x == 1:
			os.system("sudo hadoop-daemon.sh start datanode")
			input("Press Enter to Continue: ")
		elif x == 2:
			ip = input("Enter the IP: ")
			os.system("ssh root@{} sudo hadoop-daemon.sh start datanode")
			input("Press Enter to Continue: ")
		elif x == 99:
			hadoop_logo()
			hadoop_list()
		else:
			os.sysetm("echo 'Wrong Input Try Again!' | lolcat -a -d 50")
	elif slave_menu_x == 4:
		x = local_ssh()
		if x == 1:
			os.system("sudo hadoop dfsadmin -report")
			input("Press Enter to Continue: ")
		elif x == 2:
			ip = input("Enter the IP: ")
			os.system("ssh root@{} sudo hadoop dfsadmin -report".format(ip))
			input("Press Enter to Continue: ")

		elif x == 99:
			hadoop_logo()
			hadoop_list()
		else:
			os.sysetm("echo 'Wrong Input Try Again!' | lolcat -a -d 50")

	elif slave_menu_x == 5:
		hadoop_logo()
		hadoop_list()


while True:
	hadoop_logo_first()
	hadoop_list()
	if hadoop_list == '1':
		os.system("clear")
		master_menu()
	elif hadoop_list == 99:
		break

	elif hadoop_list == 0:
		os.system("python3 ./menu.py")
		break
	else:
		os.system("python3 ./menu.py")
		break
os.system("echo 'Hope You Like This :) Cya! Exiting.....' | lolcat -a -d 100")
