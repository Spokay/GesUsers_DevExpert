from Models.Database import *
from Models.User import User
from Models.Role import Role


class UserDAO:

    def __init__(self):
        # initialize a db connexion as an attribute in UserDAO
        self.dbConn = Database().getDbConn()

    # methods used to query the database
    def findUserByLogin(self, login):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT Users.*, Role.nom as rolename FROM Users JOIN Role ON Users.role_id = Role.role_id WHERE login = %s"
        cursor.execute(query, [login])
        res = cursor.fetchone()
        if res is not None:
            return User(res['user_id'], res['login'], res['pwd'], res['nom'], res['prenom'], Role(res['role_id'], res['rolename']))
        else:
            return False

    def findUserByNom(self, nom):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT Users.*, Role.nom as rolename FROM Users JOIN Role ON Users.role_id = Role.role_id WHERE Users.nom = %s"
        cursor.execute(query, [nom])
        res = cursor.fetchone()
        if res is not None:
            return User(res['user_id'], res['login'], res['pwd'], res['nom'], res['prenom'],
                        Role(res['role_id'], res['rolename']))
        else:
            return False

    def findAll(self):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT Users.*, Role.nom as rolename FROM Users JOIN Role ON Users.role_id = Role.role_id"
        cursor.execute(query)
        res = cursor.fetchall()
        users = []
        for user in res:
            users.append(User(user['user_id'], user['login'], user['pwd'], user['nom'], user['prenom'], Role(user['role_id'], user['rolename'])))
        if len(users) < 1:
            print("No users found")
        else:
            return users

    def create(self, userinfo):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "INSERT INTO Users (login, pwd, nom, prenom, role_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, [userinfo[0], userinfo[1], userinfo[2], userinfo[3], 1])
        self.dbConn.commit()
        if cursor.rowcount == 1:
            print("User created")
        else:
            print("Cannot create user")

    def delete(self, login):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "DELETE FROM Users WHERE login = %s;"
        cursor.execute(query, [login])
        self.dbConn.commit()
        if cursor.rowcount == 1:
            print("The user was deleted.")
        else:
            print("The user was not found.")

    def update(self, user):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "UPDATE users SET login = %s, nom = %s, prenom = %s WHERE user_id = %s"
        cursor.execute(query, [user.getLogin(), user.getName(), user.getFirstName(), user.getId()])
        self.dbConn.commit()
        if cursor.rowcount == 1:
            print("The user was updated. \n")
        else:
            print("The user was not found. \n")

    def changePassword(self, newPassword, currentUser):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "UPDATE users SET pwd = %s WHERE user_id = %s"
        cursor.execute(query, [newPassword, currentUser.getId()])
        self.dbConn.commit()
        if cursor.rowcount == 1:
            print("The password was successfully updated. \n")
        else:
            print("The user was not found. \n")