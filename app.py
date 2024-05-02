import webbrowser
import os
from time import sleep
import sys

def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.15)  
    print()

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
\x1b[38;2;0;255;58m[1] GitHub                           [4] Upcase
[2] Credentials                      [5] Capitalize                      [8] Open CMD
[3] Youtube                          [6] Lower                           [9] 

""") # Here you can add more options


choose = input("\x1b[38;2;0;255;58m>>> \x1b[0;0;0;0;00m")

# Here you can add or modify the options

if choose == "1" :
    print("Opening my Github Profile.")
    webbrowser.open('https://github.com/Loreehh')
    

f = open('test.txt','r')
if choose == "2" :
    print(" ")
    with open('test.txt') as f:
        contents = f.read()
        print(contents+"\x1b[0;0;0;0;00m")
    print(" ")
    input("\x1b[38;2;0;255;58mPress the enter key for exit! :D\x1b[0;0;0;0;00m")

if choose == "3":
    webbrowser.open('http://youtube.com')
    print(" ")
    input("\x1b[38;2;0;255;58mPress the enter key for exit! :D\x1b[0;0;0;0;00m")

if choose == "4":
    print("Enter what do you want")
    choose = input("\x1b[38;2;0;255;58m>>> \x1b[0;0;0;0;00m")
    print(choose.upper())

if choose == "5":
    print("Enter what do you want")
    choose = input("\x1b[38;2;0;255;58m>>> \x1b[0;0;0;0;00m")
    print(choose.capitalize())

if  choose == "6":
    print("Enter what do you want")
    choose = input("\x1b[38;2;0;255;58m>>> \x1b[0;0;0;0;00m")
    print(choose.lower())

if choose == "8":
    line_1 = "Opening Command Prompt ....."
    typewriter_effect(line_1)
    os.system("start cmd")

