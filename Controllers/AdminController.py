from Controllers.Controller import Controller
from Models.UserDAO import UserDAO

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
        nomVal = input("Enter un Nom :\n")
        user = UserDAO().findUserByNom(nomVal)
        if user is not False:
            print(f"Id: {user.getId()} \n Login: {user.getLogin()} \n Nom: {user.getName()} \n Prenom: {user.getFirstName()} \n Role: {user.getRole().getName()}")
        else:
            print("Name doesn't exist")

        keepGoing = input("Do you want to find another user : yes or no")
        if keepGoing == "yes" or keepGoing == "YES" or keepGoing == "y":
            self.showUser()

    def showAll(self):
        print("show all user")

    def exitCode(self):
        exit("I will exit")
