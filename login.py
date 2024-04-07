print('\033[92mInsert your username')
username = input('\033[94m')

print('\033[92mInsert your password')
password = input()
if username == "admin":
	if password == "1234":
		print("\033[92mAccess Granted")
	elif password != "1234":
		print("\033[93mAccess Denied")
else:
	print("\033[93mAccess Denied")


print("\033[92mWhat do you want to do?")
choose = input()

if choose == "close":
	print("\033[93mClosing Menu")
