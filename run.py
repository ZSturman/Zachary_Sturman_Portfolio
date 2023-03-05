from app import create_app
from config import DevelopmentConfig, ProductionConfig, TestingConfig


app = create_app(config_class=DevelopmentConfig)


#if __name__ == "__main__":
#    app.run()