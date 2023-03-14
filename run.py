from app import create_app, db
from config import DevelopmentConfig, ProductionConfig, TestingConfig
from pathlib import Path

app = create_app(config_class=ProductionConfig)
app.config.from_object('config.ProductionConfig')

if __name__ == "__main__":
    app.run()