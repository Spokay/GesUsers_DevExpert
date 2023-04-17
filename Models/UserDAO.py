from Models.Database import *
from Models.User import User
from Models.Role import Role
from Models.BannedIp import BannedIp
import datetime


class UserDAO:

    def __init__(self):
        # initialize a db connexion as an attribute in UserDAO
        self.dbConn = Database().getDbConn()

    # methods used to query the database :

    # this method uses a MySQL request to search the user with his login
    def findUserByLogin(self, login):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT Users.*, Role.nom as rolename FROM Users JOIN Role ON Users.role_id = Role.role_id WHERE login = %s"
        cursor.execute(query, [login])
        res = cursor.fetchone()
        if res is not None:
            return User(res['user_id'], res['login'], res['pwd'], res['nom'], res['prenom'],
                        Role(res['role_id'], res['rolename']))
        else:
            return False

    # this method uses a MySQL request to search the user with his name
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

    # this method uses a MySQL request to find every user in the database
    def findAll(self):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT Users.*, Role.nom as rolename FROM Users JOIN Role ON Users.role_id = Role.role_id"
        cursor.execute(query)
        res = cursor.fetchall()
        # it then proceeds to return every users information with their information
        if cursor.rowcount < 1:
            print("No users found")
        else:
            users = []
            for user in res:
                users.append(User(user['user_id'], user['login'], user['pwd'], user['nom'], user['prenom'],
                                  Role(user['role_id'], user['rolename'])))
            return users

    # this method creates a new user with the data it receives as 'userinfo'
    def create(self, userinfo):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "INSERT INTO Users (login, pwd, nom, prenom, role_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, [userinfo[0], userinfo[1], userinfo[2], userinfo[3], 1])
        self.dbConn.commit()
        if cursor.rowcount != 1:
            return False

    # this method will delete any user by giving his login into a MySQL request
    def delete(self, login):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "DELETE FROM users WHERE login = %s"
        cursor.execute(query, [login])
        self.dbConn.commit()
        if cursor.rowcount == 1:
            print("The user was deleted.")
        else:
            print("The user was not found.")

    # this method will update any user by giving his login into a MySQL request
    def update(self, user):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "UPDATE users SET login = %s, nom = %s, prenom = %s WHERE user_id = %s"
        cursor.execute(query, [user.getLogin(), user.getName(), user.getFirstName(), user.getId()])
        self.dbConn.commit()
        if cursor.rowcount == 1:
            print("The user was updated. \n")
        else:
            print("The user was not found. \n")

    # this method will change the password of any user with a MySQL request
    def changePassword(self, newPassword, currentUser):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "UPDATE users SET pwd = %s WHERE user_id = %s"
        cursor.execute(query, [newPassword, currentUser.getId()])
        self.dbConn.commit()
        if cursor.rowcount == 1:
            print("The password was successfully updated.")
        else:
            print("The user was not found. \n")

    def banIp(self, ip):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        current = datetime.datetime.now()
        fiveMins = current + datetime.timedelta(seconds=500)
        query = "INSERT INTO banned_ip (ip_address, countdown) VALUES (%s, %s)"
        cursor.execute(query, [ip, fiveMins])
        self.dbConn.commit()

    def checkIp(self, ip):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT * FROM banned_ip WHERE ip_address = %s"
        cursor.execute(query, [ip])
        res = cursor.fetchone()
        if res is not None:
            return BannedIp(res['id_banned_ip'], res['ip_address'], res['countdown'])
        else:
            return False

    def deleteIp(self, ip):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "DELETE FROM banned_ip WHERE ip_address = %s"
        cursor.execute(query, [ip])
        self.dbConn.commit()
