from Controllers.Controller import Controller
from Models.UserDAO import UserDAO


class UserController(Controller):

    def __init__(self, user):
        super().__init__(user)

        # Initializing User menus with specific methods
        self.menus = {
            1: {"method": self.showUser, "option-name": "Show a user's information"},
            2: {"method": self.changePassword, "option-name": "Change password"},
            2: {"method": self.exitCode, "option-name": "Exit"}
        }

    def showUser(self):
        nomVal = input("Enter un Nom :\n")
        user = UserDAO().findUserByNom(nomVal)
        if user is not False:
            self.printUserInfo(user)
        else:
            print("Name doesn't exist")

        keepGoing = input("Do you want to find another user ? (yes/YES/y) or not ? (anything else) \n")
        if self.keepGoingOrNot(keepGoing):
            self.showUser()

    def changePassword(self):
        keepGoing = input("Another password will be generated, are you sure you want to change password ? (yes/YES/y) or not ? (anything else) \n")
        if self.keepGoingOrNot(keepGoing):
            newPassword = self.generatePassword()
            UserDAO().changePassword(newPassword, self.currentUser)
