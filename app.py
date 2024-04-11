import webbrowser





print("Menu App")
choose = input()

if choose == "close" :
    print("Program closed.")

f = open('test.txt','r')
if choose == "credentials" :
    with open('test.txt') as f:
        contents = f.read()
        print(contents)

if choose == "youtube":
    webbrowser.open('http://youtube.com')








