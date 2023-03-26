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
        currentUser = user

    # Choose an option from the menus
    def chooseMenuOption(self, inputValue):
        self.menus[int(inputValue)]['method']()

    # show the menus and ask for the choice of the user
    def displayMessage(self):
        for option in self.menus:
            print(f"{option}. {self.menus[option].get('option-name')}")

        inputValue = input("Choose option :\n")
        self.chooseMenuOption(inputValue)

    # Check if a user is logged
    def isLogged(self):
        return True if self.currentUser is not None else False

    def isAdmin(self):
        return True if self.currentUser.role.name == "Admin" else False
