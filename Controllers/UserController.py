from Controllers.Controller import Controller


class UserController(Controller):
    menus = None

    def __init__(self):
        super().__init__()

        # Initializing User menus with specific methods
        self.menus = {
            1: self.testFn,
            2: self.exitCode
        }
        print(self.menus)

    def getMenu(self, inputValue):
        if self.isLogged() and self.isAdmin():
            return
        elif self.isLogged() and self.isAdmin() is not True:
            return
        else:
            self.menus[int(inputValue)]()

    def testFn(self):
        print("ouai ouai")

    def exitCode(self):
        exit("I will exit")
