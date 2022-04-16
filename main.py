#!/usr/bin/python3
import os
from platform import system

def logo():
	print("""\033[33m
	
██████╗ ██╗   ██╗███╗   ██╗ █████╗ ███╗   ███╗██╗ ██████╗███████╗
██╔══██╗╚██╗ ██╔╝████╗  ██║██╔══██╗████╗ ████║██║██╔════╝██╔════╝
██║  ██║ ╚████╔╝ ██╔██╗ ██║███████║██╔████╔██║██║██║     ███████╗
██║  ██║  ╚██╔╝  ██║╚██╗██║██╔══██║██║╚██╔╝██║██║██║     ╚════██║
██████╔╝   ██║   ██║ ╚████║██║  ██║██║ ╚═╝ ██║██║╚██████╗███████║
╚═════╝    ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝ ╚═════╝╚══════╝
																
\033[32m        A Menu Driven Python Automation Tool.
\033[34m                     :Authors:
\033[34m[✔] Rishyani Bhattacharya (https://www.linkedin.com/in/rishyani-bhattacharya-6414b8194/)
\033[34m[✔] Dipaditya Das         (https://www.linkedin.com/in/dipadityadas/)
\033[34m[✔] Alok Raj              (https://www.linkedin.com/in/alok-rithvik/)
\033[34m[✔] Niket Ranjan          (https://www.linkedin.com/in/niket24/)
\033[34m[✔] Abhishek Anand        (https://www.linkedin.com/in/abhishek-anand-88576a1a4/)
\033[97m """)

def color(c):
	os.system('tput setaf {}'.format(c))

def clear():
	os.system('clear')

def main():
	logo()
	color(6)
	input("Press any key to continue....")

	while True:
		clear()
		color(7)
		print('\n\t\t\t    Main Menu')
		print('\t\t==================================\n')
		print("""
    [1] Hadoop 
    [2] Docker 
    [3] AWS CLI
    [4] Basic Linux
    [5] SSH
\033[91m	[99] Exit From The Software
\033[97m """)
		x = int(input("Choice =>> "))
		if x == 1:
			os.system("python3 ./hadoop.py")
		elif x == 2:
			os.system("python3 ./docker.py")
		elif x == 3:
			os.system("python3 ./aws.py")
		elif x == 4:
			os.system("python3 ./basic_linux.py")
		elif x == 99:
			os.system("echo 'Hope You Like This :) Cya! Exiting.....' | lolcat -a -d 100")
			exit()
		else:
			print("Invalid Input")

main()
