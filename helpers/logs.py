from CONSTANTS import LOGS

def lprint(*args):
    with open(LOGS, "a", encoding="utf-8") as file:
        for arg in args:
            print(arg)
            file.write(arg+'\n')
    file.write("\n")