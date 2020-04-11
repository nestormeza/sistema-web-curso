from sqlalchemy import create_engine
from config import DevelopmentConfig
from flask_login import current_user

class queries():

    def Name_user():
        engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
        con = engine.connect()
        sql ='SELECT CONCAT(UPPER(LEFT(SUBSTRING_INDEX(Name," ",1),1)),LOWER(SUBSTRING(SUBSTRING_INDEX(Name," ",1),2))," ",CONCAT(UPPER(LEFT(SUBSTRING_INDEX(Last_Name," ",1),1)),LOWER(SUBSTRING(SUBSTRING_INDEX(Last_Name," ",1),2))))  AS Name  FROM users where id= %b'
        data=current_user.id
        rs = con.execute(sql,data)
        Nombre = rs.fetchone()
        Name=Nombre['Name']
        con.close()
        return Name

    def Users_list():
        engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
        con = engine.connect()
        rs = con.execute('SELECT id,LOWER(Name) AS Name,LOWER(Last_Name) AS Last_Name,Account_Type,User_Name FROM users')
        Users = rs.fetchall()
        con.close()
        return Users
