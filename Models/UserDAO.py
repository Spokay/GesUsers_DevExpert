from Models.Database import *
from Models.User import User


class UserDAO:

    def __init__(self):
        self.dbConn = Database().getDbConn()

    def findUserByLogin(self, login):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT * FROM Users WHERE login = %s"
        stmt = cursor.execute(query, [login])
        res = cursor.fetchone()
        if res != 1:
            return User(res['user_id'], res['login'])
        else:
            print("query failed")
            return False

    def findUserById(self):
        pass

    def findAll(self):
        return

    def findContentById(self, user_id):
        return

    def findContentByDate(self, date):
        return

    def findContentByKeywords(self, keyword):
        return

    def create(self, Content):
        return

    def delete(self, user_id):
        return
