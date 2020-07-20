import time
from sys import platform
import os


def creating_logs():
    while True:
        time_string = time.strftime("%Y%m%d-%H%M%S")
        filename = "log_" + str(time_string) + ".log"
        file = open(filename, 'w+')
        file.write(filename)
        file.close()
        time.sleep(5)


if platform == "linux" or platform == "linux2":
    path = r"/var/log/"
    os.chdir(path)
    creating_logs()
elif platform == "darwin":
    creating_logs()
elif platform == "win32":
    creating_logs()
