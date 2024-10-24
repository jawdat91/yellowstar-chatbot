import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
SENDGRID_SMTP_SERVER = os.getenv('SENDGRID_SMTP_SERVER')
SENDGRID_SMTP_PORT = int(os.getenv('SENDGRID_SMTP_PORT'))
SENDGRID_USERNAME = os.getenv('SENDGRID_USERNAME')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
EMAIL_FROM = os.getenv('EMAIL_FROM')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
HR_EMAIL = os.getenv('HR_EMAIL')

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
