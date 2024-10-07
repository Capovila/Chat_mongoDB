class User:
    def __int__(self, nickname: str):
        self.nickname = nickname

    def __init__(self, nickname: str, email: str, password: str):
        self.nickname = nickname
        self.email = email
        self.password = password


class Message:
    def __init__(self, email_from: str, email_to: str, content: str):
        self.email_from = email_from
        self.email_to = email_to
        self.content = content
