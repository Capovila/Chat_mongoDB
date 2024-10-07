class User:
    def __int__(self, nickname: str):
        self.nickname = nickname

    def __init__(self, nickname: str, email: str, password: str):
        self.nickname = nickname
        self.email = email
        self.password = password


class Message:
    def __init__(self, nickname_from: str, nickname_to: str, content: str):
        self.nickname_from = nickname_from
        self.nickname_to = nickname_to
        self.content = content
