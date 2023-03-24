import mysql.connector


class Database:
    def __init__(self):
        self.__dbConn = None
        self.setDbConn()

    def setDbConn(self):
        self.__dbConn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

    def getDbConn(self):
        return self.__dbConn
