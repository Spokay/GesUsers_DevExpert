class Controller:

    def getMenu(self):
        if self.isLogged() and self.isAdmin():
            return
        elif self.isLogged() and self.isAdmin() is not True:
            return
        else:
            return

    def displayMessage(self, inputValue):
        self.getMenu()

    def isLogged(self):
        pass

    def isAdmin(self):
        pass
