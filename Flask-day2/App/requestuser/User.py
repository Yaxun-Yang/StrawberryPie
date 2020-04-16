class User():
    def __init__(self, username, roomnum, token):
        self.username = username
        self.roomnum = roomnum
        self.token = token

    def updateuser(self, username, roomnum):
        self.username = username
        self.roomnum = roomnum

    def update_user(self, username, roomnum, token):
        self.username = username
        self.roomnum = roomnum
        self.token = token