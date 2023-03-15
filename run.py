from app import create_app
from config import DevelopmentConfig, ProductionConfig, TestingConfig

app = create_app(config_class=ProductionConfig)
app.config.from_object('config.ProductionConfig')

if __name__ == "__main__":
    app.run()