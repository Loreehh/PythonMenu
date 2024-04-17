import webbrowser

print(r"""
 $$$$$$\                            $$\      $$\                               
$$  __$$\                           $$$\    $$$ |                              
$$ /  $$ | $$$$$$\   $$$$$$\        $$$$\  $$$$ | $$$$$$\  $$$$$$$\  $$\   $$\ 
$$$$$$$$ |$$  __$$\ $$  __$$\       $$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$ |  $$ |
$$  __$$ |$$ /  $$ |$$ /  $$ |      $$ \$$$  $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |\$  /$$ |$$   ____|$$ |  $$ |$$ |  $$ |
$$ |  $$ |$$$$$$$  |$$$$$$$  |      $$ | \_/ $$ |\$$$$$$$\ $$ |  $$ |\$$$$$$  |
\__|  \__|$$  ____/ $$  ____/       \__|     \__| \_______|\__|  \__| \______/ 
          $$ |      $$ |                                                       
          $$ |      $$ |                                                       
          \__|      \__|                                        Made by Loreeh_                                                    
    """)


print("\x1b[0;0;0;0;00mWhat do you want to do?")


choose = input("\x1b[38;2;0;255;58m>>> ")

if choose == "close" :
    print("Program closed.")

f = open('test.txt','r')
if choose == "credentials" :
    with open('test.txt') as f:
        contents = f.read()
        print(contents+"\x1b[0;0;0;0;00m")

if choose == "youtube":
    webbrowser.open('http://youtube.com')

