from Models.UserDAO import UserDAO


def launchAuth():
    authsuccess = False
    loginVal = input("Enter login")
    user = UserDAO().findUserByLogin(loginVal)
    if user is not False:
        authsuccess = True
        print(user.getLogin())
        passwordVal = input("Enter password")

    else:
        print("Login doesn't exist")

    return authsuccess


class Controller:
    def __init__(self):
        pass

    currentUser = None

    def getMenu(self, inputValue):
        pass

    def displayMessage(self, inputValue):
        self.getMenu(inputValue)

    def isLogged(self):
        return True if self.currentUser is not None else False

    def isAdmin(self):
        return True if self.currentUser.role.name == "Admin" else False
