import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Gunicorn configuration
bind = '0.0.0.0:8000'
workers = 3
chdir = os.path.abspath(os.path.dirname(__file__))
module = 'run:app'

