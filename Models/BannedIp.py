class BannedIp:
    def __init__(self, id_banned_ip, ip_address, countdown):
        self.__id_banned_ip = id_banned_ip
        self.ip_address = ip_address
        self.__countdown = countdown

    def getId(self):
        return self.__id_banned_ip

    def getIpAddress(self):
        return self.ip_address

    def getCountdown(self):
        return self.__countdown
