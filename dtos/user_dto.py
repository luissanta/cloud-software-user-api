class UserDTO:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def from_json(json_dct):
        return UserDTO(json_dct['username'],
                       json_dct['password'])
