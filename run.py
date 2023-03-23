from app import create_app
from config import ProductionConfig

app = create_app(config_class=ProductionConfig)
app.config.from_object('config.ProductionConfig')

if __name__ == "__main__":
    app.run()