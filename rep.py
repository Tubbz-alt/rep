from sys import argv, platform
import os

script = argv
name = str(script[0])

linuxcmd = "xdg-open message.txt"
wincmd   = "start message.txt"
maccmd   = "open message.txt"

if platform == "linux" or platform == "linux2":
    os.system(linuxcmd)
    os.mkdir('clone')
    os.system("cp message.txt /clone/")
    os.system("cp " + name + " /clone/")
elif platform == "darwin":
    os.system(maccmd)
    os.mkdir('clone')
    os.system("cp message.txt /clone/")
    os.system("cp " + name + " /clone/")
elif platform == "win32":
    os.system(wincmd)
    os.mkdir('clone')
    os.system("copy message.txt C:/clone")
    os.system("copy " + name + " C:/clone")
