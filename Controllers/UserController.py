from hashlib import md5
from Controllers.Controller import Controller
from Models.UserDAO import UserDAO
from Controllers.FileController import FileController


class UserController(Controller):

    def __init__(self, user):
        super().__init__(user)

        # Initializing User menus with specific methods
        self.menus = {
            # 1: {"method": self.showUser, "option-name": "Show a user's information"},
            1: {"method": self.changePassword, "option-name": "Change password"},
            2: {"method": self.openFileExplorer, "option-name": "Open file explorer"},
            3: {"method": self.exitCode, "option-name": "Exit"}
        }
    # Regenrate a new password 
    def changePassword(self):
        keepGoing = input(
            "Another password will be generated, are you sure you want to change password ? (yes/YES/y) or not ? ("
            "anything else) \n")
        if self.keepGoingOrNot(keepGoing):
            newPassword = self.generatePassword().encode()
            UserDAO().changePassword(md5(newPassword).hexdigest(), self.currentUser)
            print(f"Your new password will be : {newPassword} \n")

    # Show User menu 
    def openFileExplorer(self):
        FileController(self.currentUser, self).run()
