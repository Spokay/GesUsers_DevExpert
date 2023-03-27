import mysql.connector


class Database:
    __dbConn = None

    def __init__(self):
        self.setDbConn()

    def setDbConn(self):

        conn = mysql.connector.connect(
            user='root',
            password='',
            host='127.0.0.1',
            port='3306',
            database='gesusers'
        )
        self.__dbConn = conn

    def getDbConn(self):
        return self.__dbConn

    def disconnect_database(self):
        self.__dbConn.close()
