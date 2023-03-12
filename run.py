from app import create_app, db
from config import DevelopmentConfig, ProductionConfig, TestingConfig, get_settings
from pathlib import Path

app = create_app(config_class=DevelopmentConfig)
app.config.from_object('config.DevelopmentConfig')

if __name__ == "__main__":
    app.run()