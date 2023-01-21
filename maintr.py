import requests
import datetime
import time
from whatsapp import Client

# WhatsApp API token
token = "API_TOKEN"

# Döviz kur API'si
exchange_rate_api = "https://openexchangerates.org/api/latest.json?app_id=API_KEY"

# Kullanıcı telefon numarası
user_phone = "+1234567890"

# Kullanıcıya gönderilecek mesaj
message = "Bugünün döviz kurları: "

def get_exchange_rate():
    response = requests.get(exchange_rate_api)
    rates = response.json()["rates"]
    return rates

def send_message(client, message):
    client.send_message(user_phone, message)

def main():
    client = Client(token)
    while True:
        current_time = datetime.datetime.now().time()
        morning_time = datetime.time(9, 0)
        evening_time = datetime.time(17, 0)

        if current_time > morning_time
