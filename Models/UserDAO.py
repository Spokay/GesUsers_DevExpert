from Models.Database import *


class UserDAO:
    def __init__(self):
        self.dbConn = Database().getDbConn()

    def findAll(self):
        return

    def findContentById(self, id):
        return

    def findContentByDate(self, date):
        return

    def findContentByKeywords(self, keyword):
        return

    def findContentByUser(self, User):
        return

    def create(self, Content):
        return

    def delete(self, id):
        return