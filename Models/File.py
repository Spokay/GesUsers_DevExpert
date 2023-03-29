class File:
    def __init__(self, file_id, filename, allowedUser):
        self.__file_id = file_id
        self.__filename = filename
        self.__allowedUser = allowedUser

    def setId(self, file_id):
        self.__file_id = file_id

    def setFileName(self, filename):
        self.__filename = filename

    def setAllowedUser(self, allowedUser):
        self.__allowedUser = allowedUser

    def getId(self):
        return self.__file_id

    def getFileName(self):
        return self.__filename

    def getAllowedUser(self):
        return self.__allowedUser
