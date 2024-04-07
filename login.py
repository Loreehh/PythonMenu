print("Inster your username")
username = input()

print("Insert your password")
password = input()
if username == "admin":
	if password == "1234":
		print("Access Granted")
	elif password != "1234":
		print("Access Denied")
else:
	print("Access Denied")