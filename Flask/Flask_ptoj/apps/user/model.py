class User:
    def __init__(self, username, password, phone = None):
        self.username = username
        self.password = password
        self.phone = phone

    def __str__(self):
        print(self.username)
