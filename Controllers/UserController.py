from Controllers.Controller import Controller


class UserController(Controller):

    def __init__(self, user):
        super().__init__(user)

        # Initializing User menus with specific methods
        self.menus = {
            1: self.testFn,
            2: self.exitCode
        }

    def testFn(self):
        print("ouai ouai")

    def exitCode(self):
        exit("I will exit")
