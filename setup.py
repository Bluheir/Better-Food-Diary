import time
import os

def setup():
    print("[ ! ] Run once only!")
    f = open("foodlog.txt", "x")
    f.close()
    time.sleep(3.5)
    os.remove("setup.py")

setup()