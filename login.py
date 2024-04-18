import os

print('\033[92mInsert your username\033[0m')
username = input('\033[94m\033[0m')

print('\033[92mInsert your password\033[0m')
password = input()
if username == "admin":

	if password == "1234":
		print("\033[92mAccess Granted")
		x = open("test.txt", "w+")
		x.write(f"Username: {username}\nPassword: {password}")

	elif password != "1234":
		print("\033[93mAccess Denied\033[0m")

else:
	print("\033[93mAccess Denied\033[0m")


print("\033[92mWhat do you want to do?\033[0m")

print("""
\x1b[38;2;0;255;58m[1] Close
[2] Menu
	  """)

choose = input("\x1b[38;2;0;255;58m>>> \x1b[0;0;0;0;00m")

if choose == "close":
	print("\033[93mClosing Menu\033[0m")

if choose == "menu":
	print("\033[93mOpening Menu\033[0m")
	os.startfile("app.py")
	
