class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = True
    # Add any other configurations you need

class ProductionConfig(Config):
    DEBUG = False
    # Production specific configuration

class DevelopmentConfig(Config):
    DEBUG = True
    # Development specific configuration