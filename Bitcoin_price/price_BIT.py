import requests

URL = 'http://api.coinmarketcap.com/v1/ticker/'  # на 16 февраля 2021 данная ссылка работает
COIN = "bitcoin"
last_price = None


def scrape():
    response = requests.get(URL+COIN)
    response_json = response.json()
    return float(response_json[0]['price_usd']) 

while True:
    latest_price = scrape()
    if latest_price != last_price:
        print("", latest_price)
        last_price = latest_price