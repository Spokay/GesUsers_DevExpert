from Controllers.Controller import Controller
from Models.FileDAO import FileDAO
from os.path import dirname, abspath


class FileController(Controller):

    def __init__(self, user, loggedUserController):
        super().__init__(user)
        self.loggedUserController = loggedUserController
        self.menus = {
            1: {"method": self.createFile, "option-name": "Create file"},
            2: {"method": self.viewFiles, "option-name": "View files"},
            3: {"method": self.exitCode, "option-name": "Exit"}
        }
        self.fileDirectory = "/ressources/"

    def createFile(self):
        filename = input("Choose a file name : \n")
        parentDir = dirname(dirname(abspath(__file__)))
        fileCreated = open(parentDir + "\\ressources\\" + filename, "x")
        keepGoing = input("Do you want fill the file content now ? (yes/YES/y) or not ? (anything else) \n")
        if self.keepGoingOrNot(keepGoing):
            self.writeInFile(fileCreated)
        FileDAO().create(filename, self.currentUser)

    def viewFiles(self):
        filesAllowed = FileDAO().findFilesForUserId(self.currentUser.getId(), self.isAdmin())
        if filesAllowed is not None:
            print(f"ID | Filename | Users allowed | Created At | Updated At")
            for file in filesAllowed:
                if file.getAllowedUsers() is not None:
                    allowedUsers = ' '.join(e.getLogin() for e in file.getAllowedUsers())
                    print(
                        f"{file.getId()} | {file.getFileName()} | {allowedUsers or ''} | {file.getCreatedAt()} | {file.getUpdatedAt()}")

            input("Type anything to quit view mode")
        else:
            print("You have no files")

    def writeInFile(self, file):
        content = input("Write content in the file : \n")
        file.write(content)

    def exitCode(self):
        self.loggedUserController.run()
