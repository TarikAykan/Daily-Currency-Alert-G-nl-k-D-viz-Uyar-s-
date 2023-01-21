import requests
import datetime
import time
from whatsapp import Client

# WhatsApp API token
token = "API_TOKEN"

# Exchange rate API
exchange_rate_api = "https://openexchangerates.org/api/latest.json?app_id=API_KEY"

# User's phone number
user_phone = "+123546549879"

# Message to be sent to the user
message = "Today's exchange rates: "

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

        if current_time > morning_time and current_time < evening_time:
        rates = get_exchange_rate()
        message += "USD: " + str(rates["USD"]) + " EUR: " + str(rates["EUR"]) + " GBP: " + str(rates["GBP"])
        send_message(client, message)
        time.sleep(3600) # Send message every hour
    else:
        time.sleep(900) # Check again after 15 minutes
