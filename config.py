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
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DSN=os.getenv("DB_DSN")
HR_EMAIL = os.getenv('HR_EMAIL')


TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
CLS_USER_ID=int(os.getenv('CLS_USER_ID'))
CLS_TELEGRAM_ID=os.getenv('CLS_TELEGRAM_ID')
CLS_MANAGERID= os.getenv('CLS_MANAGERID')
CLS_EMAIL=os.getenv('CLS_EMAIL')

USER_NAME=os.getenv('USER_NAME')