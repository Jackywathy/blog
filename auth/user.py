class User:
    def __init__(self,
                 username, password,
                 first_name, middle_names, last_name,
                 email, access_level
                 ):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.middle_names = middle_names
        self.last_name = last_name
        self.email = email
        self.access_level = access_level

    def ensure_database_consistency(self):
        

    @staticmethod
    def get_user( username, password):
