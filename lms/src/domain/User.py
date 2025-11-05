class User:
    def __init__(self, name, email, address, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return f"User: {self.id}, {self.name}, {self.email}, {self.address}"