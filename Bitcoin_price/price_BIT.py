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


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'Здесь должен быть Ваш Api-key',  # Получить его можно 
}                                       #   зарегнистрировавшысь на coinmarketcap, в личном кабинете

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e) # 
