class User:
    def __init__(self, user_id, login, psw):
        self.__psw = None
        self.__login = None
        self.__user_id = None
        self.setId(user_id)
        self.setLogin(login)
        self.setPsw(psw)

    def setId(self, user_id):
        self.__user_id = user_id

    def setLogin(self, login):
        self.__login = login

    def setPsw(self, psw):
        self.__psw = psw

    def getId(self):
        return self.__user_id

    def getLogin(self):
        return self.__login

    def getPsw(self):
        return self.__psw
