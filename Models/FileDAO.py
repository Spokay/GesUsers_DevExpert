from Models.Database import *
from Models.User import User
from Models.Role import Role
from Models.File import File


class FileDAO:

    def __init__(self):
        # initialize a db connexion as an attribute in FileDAO
        self.dbConn = Database().getDbConn()

    # find a file allowed by user id or every file if the user is an admin
    def findFilesForUserId(self, user_id, isAdmin):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT * FROM file" if isAdmin else "SELECT f.*, u.* FROM file f JOIN access a JOIN users u ON f.file_id = a.file_id AND a.user_id = u.user_id WHERE a.user_id = " + str(
            user_id)
        cursor.execute(query)
        res = cursor.fetchall()
        if cursor.rowcount >= 1:
            files = []
            for file in res:
                usersAllowed = self.findUserAllowedForFileId(file['file_id'])
                files.append(
                    File(file['file_id'], file['filename'], usersAllowed, file['created_at'], file['updated_at']))

            return files
        else:
            print("No files found")


    # find the user allowed for a specific file
    def findUserAllowedForFileId(self, file_id):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "SELECT u.*, r.nom as rolename FROM users u JOIN access a JOIN role r ON a.user_id = u.user_id AND u.role_id = r.role_id WHERE a.file_id = %s"
        cursor.execute(query, [file_id])
        res = cursor.fetchall()

        if cursor.rowcount >= 1:
            users = []
            for user in res:
                users.append(User(user['user_id'], user['login'], user['pwd'], user['nom'], user['prenom'],
                                  Role(user['role_id'], user['rolename'])))

            return users

    # add a file occurence in the database and the access to it
    def create(self, filename, creator):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "INSERT INTO file (filename, created_at, updated_at) VALUES (%s, NOW(), NOW())"
        cursor.execute(query, [filename])
        self.dbConn.commit()

        if cursor.rowcount == 1:
            print("File created")
            lastid = cursor.lastrowid
            query = "INSERT INTO access (user_id, file_id) VALUES (%s, %s)"
            cursor.execute(query, [creator.getId(), lastid])
            self.dbConn.commit()
        else:
            print("Cannot create file")

    # delete a file in the database
    def delete(self, file_id):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "DELETE FROM file WHERE file_id = %s"
        cursor.execute(query, [file_id])
        self.dbConn.commit()

        if cursor.rowcount == 1:
            print("File deleted")
        else:
            print("Cannot delete file")

    # give access to a file for a user by login
    def giveAccessToUserLogin(self, userid, fileid):
        cursor = self.dbConn.cursor(dictionary=True, prepared=True)
        query = "INSERT INTO access (user_id, file_id) VALUES (%s, %s)"
        cursor.execute(query, [userid, fileid])
        self.dbConn.commit()

        if cursor.rowcount == 1:
            print("Access given")
        else:
            print("Cannot give access")
