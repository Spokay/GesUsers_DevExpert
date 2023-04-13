from hashlib import md5
from Controllers.Controller import Controller
from Models.UserDAO import UserDAO
from Controllers.FileController import FileController


class AdminController(Controller):

    def __init__(self, user):
        super().__init__(user)

        # Initializing User menus with specific methods
        self.menus = {
            1: {"method": self.createUser, "option-name": "Create user"},
            2: {"method": self.editUser, "option-name": "Edit user"},
            3: {"method": self.deleteUser, "option-name": "Delete user"},
            4: {"method": self.showUser, "option-name": "Show user by name"},
            5: {"method": self.showAll, "option-name": "Show all users"},
            6: {"method": self.openFileExplorer, "option-name": "File explorer"},
            7: {"method": self.exitCode, "option-name": "Exit"}
        }

    # Create a user
    def createUser(self):
        firstname = input("User firstname : \n")
        name = input("User name : \n")
        login = f"{firstname[0].lower()}{name.lower()}"

        if UserDAO().findUserByLogin(login) is False:
            # generate crypted password
            passwordGenerated = self.generatePassword()
            encodedpasswordVal = md5(passwordGenerated.encode()).hexdigest()

            res = UserDAO().create([login, encodedpasswordVal, name, firstname])
            if res is not False:
                print(f"User created successfully with password : {passwordGenerated}")
                input("Remember your password and type anything")

    # Edit a user's information
    def editUser(self):
        # ask for the user to edit
        login = input("Which user's do you want to edit ? (login): \n")
        user = UserDAO().findUserByLogin(login)
        if user is not False:
            # if user exists then print his info and ask which column to edit as long as you want to keep going
            self.printUserInfo(user)
            keepGoing = True
            while keepGoing is True:
                column = input("Which column do you want to edit ? \n")
                if column.capitalize() != "Id" and column.capitalize() != "Role" and column.capitalize() != "Pwd":
                    method = getattr(user, "set" + column.capitalize())
                    newVal = input("Choose a new value : \n")
                    method(newVal)
                else:
                    print("You can't edit this column \n")

                keepGoing = self.keepGoingOrNot(input("Do you want to keep editing ? (yes/YES/y) or not ? (anything "
                                                      "else) \n"))

            UserDAO().update(user)

        else:
            print("This user doesn't exist")
            keepGoing = input("Do you want to search for another user ? (yes/YES/y) or not ? (anything else) \n")
            if self.keepGoingOrNot(keepGoing):
                self.editUser()

    # Delete a user
    def deleteUser(self):
        login = input("Which user's do you want to delete (login): \n")
        confirm = input("Are you sure you want to delete this user ? (yes/YES/y) or not ? (anything else) \n")
        if self.keepGoingOrNot(confirm):
            UserDAO().delete(login)

    # Show user's information
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

    # Show all users
    def showAll(self):
        users = UserDAO().findAll()
        for user in users:
            self.printUserInfo(user)
            print("\n")

        input("Type anything to exit the view mode \n")

    def openFileExplorer(self):
        FileController(self.currentUser, self).run()
