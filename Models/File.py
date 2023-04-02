class File:
    def __init__(self, file_id, filename, allowedUsers, created_at, updated_at):
        self.__file_id = file_id
        self.__filename = filename
        self.__allowedUsers = allowedUsers
        self.__created_at = created_at
        self.__updated_at = updated_at

    def setId(self, file_id):
        self.__file_id = file_id

    def setFileName(self, filename):
        self.__filename = filename

    def setAllowedUsers(self, allowedUsers):
        self.__allowedUsers = allowedUsers

    def setCreatedAt(self, created_at):
        self.__created_at = created_at

    def setUpdatedAt(self, updated_at):
        self.__updated_at = updated_at

    def getId(self):
        return self.__file_id

    def getFileName(self):
        return self.__filename

    def getAllowedUsers(self):
        return self.__allowedUsers

    def getCreatedAt(self):
        return self.__created_at

    def getUpdatedAt(self):
        return self.__updated_at
