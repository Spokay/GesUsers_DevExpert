import os

from Controllers.Controller import Controller
from Models.FileDAO import FileDAO
from Models.UserDAO import UserDAO
from os.path import dirname, abspath
from prompt_toolkit import prompt


class FileController(Controller):

    def __init__(self, user, loggedUserController):
        super().__init__(user)
        self.loggedUserController = loggedUserController
        self.menus = {
            1: {"method": self.createFile, "option-name": "Create file"},
            2: {"method": self.readFiles, "option-name": "View files"},
            3: {"method": self.updateFiles, "option-name": "Edit files"},
            4: {"method": self.deleteFiles, "option-name": "Delete files"},
            5: {"method": self.giveAccess, "option-name": "Give access to your files"},
            6: {"method": self.exitCode, "option-name": "Exit"}
        }
        self.fileDirectory = "ressources"

    def createFile(self):
        filename = input("Choose a file name : \n")
        parentDir = dirname(dirname(abspath(__file__)))
        if filename.find('.') == -1:
            filename = ''.join([filename, '.txt'])
        fileCreated = open(parentDir + "\\"+self.fileDirectory+"\\" + filename, "x")
        keepGoing = input("Do you want fill the file content now ? (yes/YES/y) or not ? (anything else) \n")
        if self.keepGoingOrNot(keepGoing):
            self.writeInFile(fileCreated)

        fileCreated.close()
        FileDAO().create(filename, self.currentUser)

    def readFiles(self):
        filesAllowed = FileDAO().findFilesForUserId(self.currentUser.getId(), self.isAdmin())
        if filesAllowed is not None:
            print(f"N° | Filename | Users allowed | Created At | Updated At")
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
            filesDict = self.printFiles(filesAllowed)
            fileToEdit = filesDict.get(int(input("Choose a file to edit : \n")))
            parentDir = dirname(dirname(abspath(__file__)))
            lines = open(parentDir + "\\"+self.fileDirectory+"\\" + fileToEdit.getFileName(), "r")
            fileStr = ""
            for l in lines.readlines():
                fileStr += l

            lines.close()
            res = prompt("Edit this file : \n", default=fileStr)
            fileEdited = open(parentDir + "\\"+self.fileDirectory+"\\" + fileToEdit.getFileName(), "r+")
            fileEdited.seek(0)
            fileEdited.write(res)
            fileEdited.truncate()
            print("File edited successfully")
        else:
            print("You have no files")

    def deleteFiles(self):
        filesAllowed = FileDAO().findFilesForUserId(self.currentUser.getId(), self.isAdmin())
        if filesAllowed is not None:
            filesDict = self.printFiles(filesAllowed)
            fileToDelete = filesDict.get(int(input("Choose a file to delete : \n")))
            parentDir = dirname(dirname(abspath(__file__)))
            os.remove(parentDir + "\\"+self.fileDirectory+"\\" + fileToDelete.getFileName())
            FileDAO().delete(fileToDelete.getId())

    def giveAccess(self):
        filesAllowed = FileDAO().findFilesForUserId(self.currentUser.getId(), self.isAdmin())
        filesDict = self.printFiles(filesAllowed)
        fileToGive = input("Which file do you want to give access to ? : \n")
        user = UserDAO().findUserByLogin(input("Which user do you want to give access to ? (login) : \n"))
        if user is not None:
            print(filesDict.get(int(fileToGive)))
            FileDAO().giveAccessToUserLogin(user.getId(), filesDict.get(int(fileToGive)).getId())
        else:
            print("This user does not exist")

    def writeInFile(self, file):
        content = input("Write content in the file : \n")
        file.write(content)

    def exitCode(self):
        self.loggedUserController.run()

    def printFiles(self, filesAllowed):
        print(f"N° | Filename | Users allowed | Created At | Updated At")
        filesDict = {}
        i = 1
        for file in filesAllowed:
            filesDict[i] = file
            if file.getAllowedUsers() is not None:
                allowedUsers = ' '.join(e.getLogin() for e in file.getAllowedUsers())
                print(
                    f"{i} | {file.getFileName()} | {allowedUsers or ''} | {file.getCreatedAt()} | {file.getUpdatedAt()}")

            i += 1

        return filesDict
