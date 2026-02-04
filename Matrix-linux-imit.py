from random import randint
from time import sleep
import colorama
def Matrix():
    print(colorama.Fore.LIGHTGREEN_EX + " " * Space + str(BIN))
while True:
    BIN=randint(0,1)
    Space=randint(1,105)
    Rep=randint(1,4)
    while Rep > 0:
        Matrix()
        Rep -= 1
    sleep(0.1)

