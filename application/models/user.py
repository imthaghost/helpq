"""User Model"""
# built in python modules

# external python modules
import uuid
from bcrypt import hashpw, gensalt
# local python modules
import application


class User(object):
    def __init__(self, email='None', password='None'):
        self.full_name = None
        # password is not required because a user can sign up with OAUTH
        self.online = False  # intialize onilne to false
        self.uuid = None  # initalize no uuid
        self.email = email  # email will be the username
        self.password = hashpw(password.encode(
            'utf-8'), gensalt())  # set password
        self.phonenumber = None  # user phone number

    def set_uuid(self):
        self.uuid = str(uuid.uuid4())

    def serialize(self):
        # serialize user details
        return {
            "email": self.email,
            "uuid": self.uuid,
            "password": self.password,
            "fullname": self.full_name,
            "online": self.online,
            "phonenumber":  self.phonenumber
        }

    def save_new(self):
        # todo refactor to make more DRY for all Models
        # todo generate a token and sent to users email
        # saves new user to database
        application.user.insert_one(self.serialize())
