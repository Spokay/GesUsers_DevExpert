from Controllers.Controller import Controller


class FileController(Controller):

    def __init__(self, user):
        super().__init__(user)
        self.menus = {
            1: {"method": self.viewFile, "option-name": "View File"},
            7: {"method": self.exitCode, "option-name": "Exit"}
        }

    def viewFile(self):
        pass
