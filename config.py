import os
class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
	SQLALCHEMY_DATABASE_URI = 'mysql://root:925204@127.0.0.1/microblog'
	SQLALCHEMY_TRACK_MODIFICATIONS = False