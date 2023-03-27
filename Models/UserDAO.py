from Models.Database import *
from Models.User import User
from Models.Role import Role


class UserDAO:

    def __init__(self):
        self.dbConn = Database().getDbConn()

    def findUserByLogin(self, login):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT Users.*, Role.nom as rolename FROM Users JOIN Role ON Users.role_id = Role.role_id WHERE login = %s"
        stmt = cursor.execute(query, [login])
        res = cursor.fetchone()
        if res is not None:
            return User(res['user_id'], res['login'], res['pwd'], res['nom'], res['prenom'], Role(res['role_id'], res['rolename']))
        else:
            return False

    def findUserByNom(self, nom):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT Users.*, Role.nom as rolename FROM Users JOIN Role ON Users.role_id = Role.role_id WHERE Users.nom = %s"
        stmt = cursor.execute(query, [nom])
        res = cursor.fetchone()
        if res is not None:
            return User(res['user_id'], res['login'], res['pwd'], res['nom'], res['prenom'], Role(res['role_id'], res['rolename']))
        else:
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

    def create(self, user):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = f"INSERT INTO Users (user_id, login, pwd, nom, prenom, role_id) VALUES (%s, %s, %s, %s, %s, %s)"
        stmt = cursor.execute(query, [user.getId(), user.getLogin(), user.getPwd(), user.getName(), user.getFirstName(), user.getRole().getId()])

    def delete(self, user_id):
        return
