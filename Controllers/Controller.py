from Models.UserDAO import UserDAO


def launchAuth():
    authsuccess = False
    loginVal = input("Entre ton login")
    user = UserDAO().findUserByLogin(loginVal)

    passwordVal = input("Entre mot de passe")

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
