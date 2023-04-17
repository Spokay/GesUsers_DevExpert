import os

from Controllers.Controller import Controller
from Models.FileDAO import FileDAO
from Models.UserDAO import UserDAO
from os.path import dirname, abspath
from prompt_toolkit import prompt


class FileController(Controller):

    def __init__(self, user, loggedUserController):
        super().__init__(user)
        # Controller of currently logged user
        self.loggedUserController = loggedUserController
        # File Explorer Menus
        self.menus = {
            1: {"method": self.createFile, "option-name": "Create file"},
            2: {"method": self.readFiles, "option-name": "View files"},
            3: {"method": self.updateFiles, "option-name": "Edit files"},
            4: {"method": self.deleteFiles, "option-name": "Delete files"},
            5: {"method": self.giveAccess, "option-name": "Give access to your files"},
            6: {"method": self.exitCode, "option-name": "Exit"}
        }
        # directory of the files
        self.fileDirectory = "ressources"

    def createFile(self):
        # choose a file name
        filename = input("Choose a file name : \n")
        # get the parent directory
        parentDir = dirname(dirname(abspath(__file__)))
        # if the file extension is not added set it to .txt by default
        if filename.find('.') == -1:
            filename = ''.join([filename, '.txt'])

        # create the file
        fileCreated = open(parentDir + "\\" + self.fileDirectory + "\\" + filename, "x")
        keepGoing = input("Do you want fill the file content now ? (yes/YES/y) or not ? (anything else) \n")
        if self.keepGoingOrNot(keepGoing):
            # fill content in the file
            self.writeInFile(fileCreated)

        fileCreated.close()
        # add the file to the database
        FileDAO().create(filename, self.currentUser)

    def readFiles(self):
        # get the allowed files for the current user
        filesAllowed = FileDAO().findFilesForUserId(self.currentUser.getId(), self.isAdmin())
        if filesAllowed is not None:
            # print the allowed files and put them in a dict
            filesDict = self.printFiles(filesAllowed)
            # get the right file according to the input
            fileToRead = filesDict.get(int(input("Choose a file to read : \n")))
            parentDir = dirname(dirname(abspath(__file__)))
            lines = open(parentDir + "\\" + self.fileDirectory + "\\" + fileToRead.getFileName(), "r")
            fileStr = ""
            # loop threw the files lines and add them to a string
            for line in lines.readlines():
                fileStr += line + "\n"

            lines.close()
            # print the file content
            print("File content : \n", fileStr)
            input("Type anything to quit view mode")
        else:
            print("You have no files")

    def updateFiles(self):
        # get the allowed files for the current user
        filesAllowed = FileDAO().findFilesForUserId(self.currentUser.getId(), self.isAdmin())
        if filesAllowed is not None:
            # print the allowed files and put them in a dict
            filesDict = self.printFiles(filesAllowed)
            # get the right file according to the input
            fileToEdit = filesDict.get(int(input("Choose a file to edit : \n")))
            parentDir = dirname(dirname(abspath(__file__)))
            lines = open(parentDir + "\\" + self.fileDirectory + "\\" + fileToEdit.getFileName(), "r")
            fileStr = ""
            # loop threw the files lines and add them to a string
            for line in lines.readlines():
                fileStr += line + "\n"

            lines.close()
            # start a prompt with a default value of the file content
            res = prompt("Edit this file : \n", default=fileStr)
            # replace the file content with the edited content
            fileEdited = open(parentDir + "\\" + self.fileDirectory + "\\" + fileToEdit.getFileName(), "r+")
            fileEdited.seek(0)
            fileEdited.write(res)
            fileEdited.truncate()
            print("File edited successfully")
        else:
            print("You have no files")

    def deleteFiles(self):
        # get the allowed files for the current user
        filesAllowed = FileDAO().findFilesForUserId(self.currentUser.getId(), self.isAdmin())
        if filesAllowed is not None:
            # print the allowed files and put them in a dict
            filesDict = self.printFiles(filesAllowed)
            # get the right file according to the input
            fileToDelete = filesDict.get(int(input("Choose a file to delete : \n")))
            parentDir = dirname(dirname(abspath(__file__)))
            # remove the file from the directory
            os.remove(parentDir + "\\" + self.fileDirectory + "\\" + fileToDelete.getFileName())
            # remove the file from the database
            FileDAO().delete(fileToDelete.getId())

    def giveAccess(self):
        # get the allowed files for the current user
        filesAllowed = FileDAO().findFilesForUserId(self.currentUser.getId(), self.isAdmin())
        # print the allowed files and put them in a dict
        filesDict = self.printFiles(filesAllowed)
        fileToGive = input("Which file do you want to give access to ? : \n")
        # get the user chosen to give access to him
        user = UserDAO().findUserByLogin(input("Which user do you want to give access to ? (login) : \n"))
        if user is not None:
            # give access to the user
            FileDAO().giveAccessToUserLogin(user.getId(), filesDict.get(int(fileToGive)).getId())
        else:
            print("This user does not exist")

    def writeInFile(self, file):
        # write content in a file
        content = input("Write content in the file : \n")
        file.write(content)

    def exitCode(self):
        # return to the previous menu
        self.loggedUserController.run()

    def printFiles(self, filesAllowed):
        # print the allowed files information and return a dict with them
        print(f"N° | Filename | Users allowed | Created At | Updated At")
        filesDict = {}
        i = 1
        for file in filesAllowed:
            filesDict[i] = file
            if file.getAllowedUsers() is not None:
                for allowedUser in file.getAllowedUsers():
                    print(
                        f"{i} | {file.getFileName()} | {allowedUser.getLogin() or ''} | {file.getCreatedAt()} | {file.getUpdatedAt()}")
            i += 1
        return filesDict
