class User:
    def __init__(self, content_id, text):
        self.__content_id = content_id
        self.__text = text

    def setId(self, content_id):
        self.__content_id = content_id

    def setText(self, text):
        self.__text = text

    def getId(self):
        return self.__content_id

    def getText(self):
        return self.__text
