# import requests
from requests import Session, TooManyRedirects,Timeout
import json

# URL = 'http://api.coinmarketcap.com/v1/ticker/'  # на 16 февраля 2021 данная ссылка не работает
# COIN = "bitcoin"
# last_price = None


# def scrape():
#     response = requests.get(URL+COIN)
#     response_json = response.json()
#     return float(response_json[0]['USD']) 

# while True:
#     latest_price = scrape()
#     if latest_price != last_price:
#         print("Последняя цена: ", latest_price)
#         last_price = latest_price


url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'   # Это URL для тестового АПИ.
parameters = {
    # "id": '1027',
    # 'name': "Bitcoin",
    # "symbol": "BTC",
    # "slug": "bitcoin",
    # 'id': '1',
    # 'slug': 'ETH',
    # 'symbol': '',
    'start': '1',
    'limit':'1',
    'sort':'id',
    'convert':'USD',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',    # Это тестовый АПИ. Что бы получить свой АПИ нужно 
}                                       #   зарегнистрироваться на coinmarketcap, в личном кабинете найдёте где его сгенирировать

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    data_lin = json.dumps(data, sort_keys=True)
    print(data)  # json ответ
#   print(json.dump(data, sort_keys=True))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)  # json ответ
