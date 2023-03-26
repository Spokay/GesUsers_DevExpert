from Controllers.Controller import Controller


class AdminController(Controller):

    def __init__(self, user):
        super().__init__(user)

        # Initializing User menus with specific methods
        self.menus = {
            1: {"method": self.createUser, "option-name": "Create user"},
            2: {"method": self.editUser, "option-name": "Edit user"},
            3: {"method": self.deleteUser, "option-name": "Delete user"},
            4: {"method": self.showUser, "option-name": "Show user by login or id"},
            5: {"method": self.showAll, "option-name": "Show all users"},
            6: {"method": self.exitCode, "option-name": "Exit"}
        }

    def createUser(self):
        print("create user option")

    def editUser(self):
        print("edit user option")

    def deleteUser(self):
        print("delete user option")

    def showUser(self):
        print("show user option")

    def showAll(self):
        print("show all users option")

    def exitCode(self):
        exit("I will exit")
