from Controllers import Controller
from Models.UserDAO import *


def run():
    while True:
        val = input()
        Controller().displayMessage(val)


run()
