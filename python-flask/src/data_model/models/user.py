class User():
    authenticated = False

    def authenticate(self, password):
        self.authenticated = True
        return True

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def __str__(self) -> str:
        return f"{self.name}"
