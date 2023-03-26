class Role:
    def __init__(self, role_id, name):
        self.__role_id = role_id
        self.__name = name

    def getId(self):
        return self.__role_id

    def getName(self):
        return self.__name

    def setId(self, role_id):
        self.__role_id = role_id

    def setName(self, name):
        self.__name = name
