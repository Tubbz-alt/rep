from sys import argv, platform
from multiprocessing import Process
import os

script = argv
name = str(script[0])

linuxcmd = "xdg-open message.txt"
wincmd   = "start message.txt"
maccmd   = "open message.txt"

lproc = Process(target=os.system, args=(linuxcmd,))
wproc = Process(target=os.system, args=(wincmd,))
mproc = Process(target=os.system, args=(maccmd,))

if platform == "linux" or platform == "linux2":
    lproc.start()
    os.chdir("/")
    os.mkdir("clone")
    os.system("cp message.txt clone/")
    os.system("cp " + name + " clone/")
elif platform == "darwin":
    mproc.start()
    os.chdir("/")
    os.mkdir('clone')
    os.system("cp message.txt clone/")
    os.system("cp " + name + " clone/")
elif platform == "win32":
    wproc.start()
    os.chdir('C:\\')
    os.mkdir('clone')
    os.system("copy message.txt clone")
    os.system("copy " + name + " clone")
