class Config:
    SECRET_KEY = '12.3nv123.23b4n89853hdfbnfd.436y'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/db_camara'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
config = {
    'development':DevelopmentConfig,
    'default': DevelopmentConfig
}
