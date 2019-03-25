import os
import sys

users=[]
user_passwords={}
transactions={}
current_user=''
def login():
	global users
	global user_passwords
	global current_user
	u_name=input(" Enter Username : ")	
	u_pass=input(" Enter Password : ")
	if (u_name in users and u_pass==user_passwords[u_name]):
		print("Logged in sucessfully!")
		current_user=u_name
		return 1
	else:
		print("Wrong Username or Password! Sure you have an account?")
		return 0

def signup():
	global users
	global user_passwords
	global transactions
	while(1):
		os.system('cls' if os.name == 'nt' else 'clear')
		u_name=input("Enter Preferred Username: ")
		if(u_name in users):
			print("OOPS! Username already exists.")
			temp=input("Enter 0 for previous menu or 1 to retry : ")
			if(temp==0):
				return 0
			else:
				continue
		else:
			u_pass=input("Enter Preferred Password: ")
			users.append(u_name)
			user_passwords[u_name]
			transactions[u_name]={'payable':{},'receivable':{}}
			return 1

def add_transaction():
	global users
	global transactions
	n=int(input("Enter number of people visited: "))
	total=int(input("Enter the amount spent: "))
	person={}
	get={}
	give={}
	each=total/n

	for i in range (0,n):
		p_name=print("Enter person username: ")
		p_spent=print("Enter the amount spent by person: ")
		person[p_name]=p_spent
		if(p_spent>each):
			get[p_name]=p_spent-each
		if(p_spent<each):
			give[p_name]=each-p_spent
	for i in get.keys():
		temp=get[i]/len(give.keys())
		for j in give.keys():
			if (j in transactions[i]['receivable'].keys()):
				transactions[i]['receivable'][j]=transactions[i]['receivable'][j]+temp
				


def show_ledger():
	global transactions
	global current_user
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Under Construction !!! Showing the entire ledger for now ")
	print(transactions[current_user])

print("Hello!")
while(1):
	print("Enter your choice from menu")
	choice1=int(input("1. Login \n2. Signup\n0. Exit"))
	if(choice==1):
		login_status=login()
		if(login_status==0):
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Looks like you dont have an account! Signup maybe?\n")
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Logged in sucessfully\n")
			while(1):
				choice3=int(input("Enter 1 to add transaction \n 2 to show ledger\n 3 to exit"))
				if(choice==1):
					add_transaction()
				if(choice==2):
					show_ledger()
				else:
					sys.exit()

	else if(choice==2):
		signup_status=signup()
		if(signup_status==0):
			os.system('cls' if os.name == 'nt' else 'clear')
			continue
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Sucessfully signed up!\n")
	else if(choice==0):
		print("\n\nThank you!")
		break;

