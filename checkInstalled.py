import os

def checkInstalled(dir,name): ##if name not in dir install
    return not (name in os.listdir(dir))