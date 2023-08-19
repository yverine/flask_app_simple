import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
   
    # First MySQL database configuration
    MYSQL_DATABASE_NAME = os.environ.get('MYSQL_DB_NAME_1')
    
    #same
    MYSQL_DATABASE_USER = os.environ.get('MYSQL_USER')
    MYSQL_DATABASE_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DATABASE_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_DATABASE_PORT = os.environ['MYSQL_PORT']
    print(MYSQL_DATABASE_PORT)
    
    # Second MySQL database configuration
    MYSQL_DATABASE_NAME_2 = os.environ.get('MYSQL_DB_NAME_2')
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI_1 = f"mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}:{MYSQL_DATABASE_PORT}/{MYSQL_DATABASE_NAME}"
    SQLALCHEMY_DATABASE_URI_2 = f"mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}:{MYSQL_DATABASE_PORT}/{MYSQL_DATABASE_NAME_2}"
    SQLALCHEMY_BINDS = {
        'db1': SQLALCHEMY_DATABASE_URI_1,
        'db2': SQLALCHEMY_DATABASE_URI_2
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False