import requests
from config import TELEGRAM_API_URL

class TelegramBot:
    @staticmethod
    def send_message(chat_id, text):
        url = TELEGRAM_API_URL
        payload = {'chat_id': chat_id, 'text': text}
        requests.post(url, json=payload)
