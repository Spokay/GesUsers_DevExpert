from Controllers.Controller import Controller
from Models.FileDAO import FileDAO
from os.path import dirname, abspath
from prompt_toolkit import prompt


class FileController(Controller):

    def __init__(self, user, loggedUserController):
        super().__init__(user)
        self.loggedUserController = loggedUserController
        self.menus = {
            1: {"method": self.createFile, "option-name": "Create file"},
            2: {"method": self.readFiles, "option-name": "View files"},
            2: {"method": self.updateFiles, "option-name": "Edit files"},
            2: {"method": self.deleteFiles, "option-name": "Delete files"},
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

        fileCreated.close()
        FileDAO().create(filename, self.currentUser)

    def readFiles(self):
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

    def updateFiles(self):
        filesAllowed = FileDAO().findFilesForUserId(self.currentUser.getId(), self.isAdmin())
        if filesAllowed is not None:
            print(f"ID | Filename | Users allowed | Created At | Updated At")
            filesDict = {}
            i = 1
            for file in filesAllowed:
                filesDict[i] = file
                if file.getAllowedUsers() is not None:
                    allowedUsers = ' '.join(e.getLogin() for e in file.getAllowedUsers())
                    print(
                        f"{i} | {file.getFileName()} | {allowedUsers or ''} | {file.getCreatedAt()} | {file.getUpdatedAt()}")

                i += 1
            fileToEdit = filesDict.get(int(input("Choose a file to edit : \n")))
            parentDir = dirname(dirname(abspath(__file__)))
            lines = open(parentDir + "\\ressources\\" + fileToEdit.getFileName(), "r")
            fileStr = ""
            for l in lines.readlines():
                fileStr += l

            lines.close()
            res = prompt("Edit this file : \n", default=fileStr)
            fileEdited = open(parentDir + "\\ressources\\" + fileToEdit.getFileName(), "r+")
            fileEdited.seek(0)
            fileEdited.write(res)
            fileEdited.truncate()
            print("File edited successfully")

        else:
            print("You have no files")

    def deleteFiles(self):
        pass

    def writeInFile(self, file):
        content = input("Write content in the file : \n")
        file.write(content)

    def exitCode(self):
        self.loggedUserController.run()
