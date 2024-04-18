import webbrowser

print("""
 █████  ██████  ██████      ███    ███ ███████ ███    ██ ██    ██ 
██   ██ ██   ██ ██   ██     ████  ████ ██      ████   ██ ██    ██ 
███████ ██████  ██████      ██ ████ ██ █████   ██ ██  ██ ██    ██ 
██   ██ ██      ██          ██  ██  ██ ██      ██  ██ ██ ██    ██ 
██   ██ ██      ██          ██      ██ ███████ ██   ████  ██████                                                                                        
    """)
print("\033[92mMade by Loreeh_\033[0m")
print("""
      
      
      
      
      
      """)


print("\x1b[0;0;0;0;00mWhat do you want to do?")

print("""
\x1b[38;2;0;255;58m[1] Close
[2] Credentials
[3] Youtube

""")


choose = input("\x1b[38;2;0;255;58m>>> \x1b[0;0;0;0;00m")

if choose == "close" :
    print("Program closed.")

f = open('test.txt','r')
if choose == "credentials" :
    print(" ")
    with open('test.txt') as f:
        contents = f.read()
        print(contents+"\x1b[0;0;0;0;00m")
    print(" ")
    input("\x1b[38;2;0;255;58mPress the enter key for exit! :D\x1b[0;0;0;0;00m")

if choose == "youtube":
    webbrowser.open('http://youtube.com')

