from Controllers.Controller import Controller
from Models.FileDAO import FileDAO


class FileController(Controller):

    def __init__(self, user, loggedUserController):
        super().__init__(user)
        self.loggedUserController = loggedUserController
        self.menus = {
            1: {"method": self.viewFiles, "option-name": "View File"},
            2: {"method": self.exitCode, "option-name": "Exit"}
        }

    def viewFiles(self):
        filesAllowed = FileDAO().findFilesForUserId(self.currentUser.getId())
        if filesAllowed is not None:
            for file in filesAllowed:
                allowedUsers = ' '.join(e.getLogin() for e in file.getAllowedUsers())
                print(f"ID | Filename | Users allowed | Created At | Updated At")
                print(
                    f"{file.getId()} | {file.getFileName()} | {allowedUsers} | {file.getCreatedAt()} | {file.getUpdatedAt()}")

            input("ok")
        else:
            print("You have no files")

    def exitCode(self):
        self.loggedUserController.run()
