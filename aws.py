import os
from platform import system


def aws_menu():
	if system() == 'Linux':
		os.system("clear")
		os.system("figlet -f standard -c AWS | lolcat")

	elif system() == 'Windows':
		os.system("cls")
		print(aws_logo)


aws_logo = """\033[33m

     ___        ______  
    / \ \      / / ___| 
   / _ \ \ /\ / /\___ \ 
  / ___ \ V  V /  ___) |
 /_/   \_\_/\_/  |____/ 
						
							   
	\033[97m """


def aws_list():
	print("""\033[33m
				\033[32mChoose Your Option

		\033[36m[1] Configure AWS  
		\033[36m[2] Create Key Pair
		\033[36m[3] Create Security Group  
		\033[36m[4] Launch an Instance
		\033[36m[5] Describe an Instance
		\033[91m[6] Return to Menu
	\033[97m """)

	ch = int(input("Choice ==>>  "))
	if int(ch) == 1:
		print()
		os.system("aws configure")
		input("Press Enter to continue")
	elif int(ch) == 2:
		print()
		key_name = input("Enter Key-pair Name :")
		os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
		input("Press Enter to continue")

	elif int(ch) == 3:
		print()
		sg_name = input("Enter Security Group Name : ")
		sg_desc = input("Enter the Description :")
		os.system(
			"aws ec2 create-security-group --group-name {0} --description {1}".format(sg_name, sg_desc))
		print("Add Rule to Security Group")
		protocol = input("Enter the Protocol : ")
		port = input("Enter the Port Number : ")
		cidr = input("Enter the CIDR : ")
		os.system('aws ec2 authorize-security-group-ingress --group-name {0} --protocol {1} --port {2} --cidr {3}'.format(
			sg_name, protocol, port, cidr))
		input("Press Enter to continue")
	elif int(ch) == 4:
		print()
		instance_type = input("Enter teh Instance Type : ")
		key_name = input("Enter the Key-pair Name : ")
		count = input("Enter the Count : ")
		os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type {0} --key-name {1} --subnet-id subnet-0a420fc4eb459022a --count {2}".format(
			instance_type, key_name, count))
		input("Press Enter to continue")
	elif int(ch) == 5:
		print()
		os.system("aws ec2 describe-instances")
		input("Press Enter to continue")
	elif int(ch) == 6:
		exit()
	else:
		print("Please Select right Choice")
		input()


aws_menu()
aws_list()
