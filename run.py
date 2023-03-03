from app import create_app
from config import DevelopmentConfig

app = create_app(config_class=DevelopmentConfig)
app.config.from_object('config.DevelopmentConfig')

if __name__ == "__main__":
    app.run(debug=True)