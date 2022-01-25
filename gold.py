import json
import requests
def get_price():
  headers = {
    'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
  }
  r = requests.get('https://data-asg.goldprice.org/dbXRates/USD', headers=headers)
  print(r.text)
  return round(json.loads(r.text)['items'][0]['xauPrice']*28.43685319317602) #*28.43407713416372


print(get_price())