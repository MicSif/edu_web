class BaseConfig(object):
	SECRET_KEY = 'makesure to set a very secret key'

class DevelopmentConfig(BaseConfig):
	"""Development Config"""
	DEBUG = True
	SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'

class ProductConfig(BaseConfig):
	"""Product Config"""
	pass

class TestingConfig(BaseConfig):
	"""Testing Config"""
	pass

configs = {
	'development':DevelopmentConfig,
	'production':ProductConfig,
	'testing':TestingConfig
}