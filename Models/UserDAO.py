from Models.Database import *


class UserDAO:
    def __init__(self):
        self.dbConn = Database().getDbConn()

    def text(self):
        print(self.dbConn)

