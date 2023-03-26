class User:
    def __init__(self, user_id, login, pwd, name, firstname, role):
        self.__role = role
        self.__firstname = firstname
        self.__name = name
        self.__pwd = pwd
        self.__login = login
        self.__user_id = user_id

    def setId(self, user_id):
        self.__user_id = user_id

    def setLogin(self, login):
        self.__login = login

    def setPwd(self, pwd):
        self.__pwd = pwd

    def setName(self, name):
        self.__name = name

    def setFirstName(self, firstname):
        self.__firstname = firstname

    def setRole(self, role):
        self.__role = role

    def getId(self):
        return self.__user_id

    def getLogin(self):
        return self.__login

    def getPwd(self):
        return self.__pwd

    def getName(self):
        return self.__name

    def getFirstName(self):
        return self.__firstname

    def getRole(self):
        return self.__role
