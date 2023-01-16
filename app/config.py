import os

db_host = os.environ.get('DB_HOST', default='192.168.1.172')
db_name = os.environ.get('DB_NAME', default='notes')
db_user = os.environ.get('DB_USERNAME', default='notes')
db_password = os.environ.get('DB_PASSWORD', default='notes1234')
db_port = os.environ.get('DB_PORT', default='3306')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"