from Models.UserDAO import UserDAO
from hashlib import md5


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
        return True if self.currentUser.role.name == "Admin" else False

    # print a user's information
    def printUserInfo(self, user):
        print(
            f" Id: {user.getId()} \n Login: {user.getLogin()} \n Name: {user.getName()} \n FirstName: {user.getFirstName()} \n Role: {user.getRole().getName()}")

    # check a boolean for a confirmation
    def keepGoingOrNot(self, inputVal):
        return True if inputVal == "yes" or inputVal == "YES" or inputVal == "y" else False

    def generatePassword(self):
        pass

    def exitCode(self):
        exit("I will exit")
