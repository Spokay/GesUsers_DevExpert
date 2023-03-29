from Models.Database import *
from Models.User import User
from Models.Role import Role
from Models.File import File


class FileDAO:

    def __init__(self):
        # initialize a db connexion as an attribute in UserDAO
        self.dbConn = Database().getDbConn()

    # methods used to query the database
    def findFilesForUserId(self, user_id):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT f.*, u.* FROM file f JOIN access a JOIN users u ON f.file_id = a.file_id AND a.user_id = u.user_id WHERE a.user_id = %s"
        cursor.execute(query, [user_id])
        res = cursor.fetchall()
        if cursor.rowcount >= 1:
            files = []
            for file in res:
                usersAllowed = self.findUserAllowedForFileId(file['file_id'])
                files.append(File(file['file_id'], file['filename'], usersAllowed, file['created_at'], file['updated_at']))

            return files
        else:
            print("No files found")

    def findUserAllowedForFileId(self, file_id):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT u.*, r.nom as rolename FROM users u JOIN access a JOIN role r ON a.user_id = u.user_id AND u.role_id = r.role_id WHERE a.file_id = %s"
        cursor.execute(query, [file_id])
        res = cursor.fetchall()

        if cursor.rowcount > 1:
            users = []
            for user in res:
                users.append(User(user['user_id'], user['login'], user['pwd'], user['nom'], user['prenom'],
                                  Role(user['role_id'], user['rolename'])))

            return users
        else:
            print("No user found")
