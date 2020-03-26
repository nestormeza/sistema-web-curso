from . import db

import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash



class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    Name = db.Column(db.String(40),nullable = False)
    Last_Name = db.Column(db.String(40),nullable = False)
    Account_Type = db.Column(db.String(30),nullable = False)
    User_Name = db.Column(db.String(40),unique = True,nullable = False)
    Encrypted_Password = db.Column(db.String(100),nullable = False)
    create_at = db.Column(db.DateTime,default = datetime.datetime.now())

    def verify_password(self,Password):
        return check_password_hash(self.Encrypted_Password,Password)

    @property
    def Password(self):
        pass

    @Password.setter
    def Password(self,value):
        self.Encrypted_Password= generate_password_hash(value)


    def __str__(self):
        return self.User_Name

    @classmethod
    def  create_element(cls,Name,Last_Name,Account_Type,User_Name,Password):
        user = User(Name=Name,Last_Name=Last_Name,Account_Type=Account_Type,User_Name=User_Name,Password=Password)

        db.session.add(user)
        db.session.commit()

        return user

    @classmethod
    def get_by_User_Name(cls,User_Name):
        return User.query.filter_by(User_Name=User_Name).first()

    @classmethod
    def get_by_id(cls,id):
        return User.query.filter_by(id=id).first()
