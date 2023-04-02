from Models.UserDAO import UserDAO
from hashlib import md5
import random


def launchAuth():
    loginVal = input("Enter login :\n")
    user = UserDAO().findUserByLogin(loginVal)
    if user is not False:
        encodedpasswordVal = md5(input("Enter password :\n").encode()).hexdigest()
        if encodedpasswordVal == user.getPwd():
            print(f"Welcome {user.getFirstName()} {user.getName()}")
            return user
        else:
            print("password doesn't match the login")
            return False
    else:
        print("Login doesn't exist")
        return False


class Controller:
    def __init__(self, user):
        self.menus = {}
        self.currentUser = user

    def run(self):
        while True:
            self.displayMessage()

    # Choose an option from the menus
    def chooseMenuOption(self, inputValue):
        self.menus[int(inputValue)]['method']()

    # show the menus and ask for the choice of the user
    def displayMessage(self):
        for option in self.menus:
            print(f"{option}. {self.menus[option].get('option-name')}")

        inputValue = input("Choose option :\n")
        self.chooseMenuOption(inputValue)

    # Check if the current user is logged
    def isLogged(self):
        return True if self.currentUser is not None else False

    # Check if the current user is an admin

    def isAdmin(self):
        return True if self.currentUser.getRole().getName() == "Admin" else False

    # print a user's information
    def printUserInfo(self, user):
        print(
            f" Id: {user.getId()} \n Login: {user.getLogin()} \n Name: {user.getName()} \n FirstName: {user.getFirstName()} \n Role: {user.getRole().getName()}")

    # check a boolean for a confirmation
    def keepGoingOrNot(self, inputVal):
        return True if inputVal == "yes" or inputVal == "YES" or inputVal == "y" else False

    def generatePassword(self):
        char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        length = 8
        password = ''
        for i in range(length):
            random_char = random.choice(char_seq)
            password += random_char

            # print(password)
        list_pass = list(password)
        random.shuffle(list_pass)
        final_password = ''.join(list_pass)
        return final_password

    def exitCode(self):
        exit("I will exit")
