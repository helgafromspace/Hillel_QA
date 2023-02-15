
class UserApi:
    def __init__(self,name,gender,email,status,user_id = None):
        self.name = name
        self.gender = gender
        self.email = email
        self.status = status
        self.user_id = user_id

    def json_constructor(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "email": self.email,
            "status": self.status,
            "user_id": self.user_id
        }