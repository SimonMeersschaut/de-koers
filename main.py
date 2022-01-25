from math import floor, ceil
import pandas_datareader as pdr
import json
import matplotlib.pyplot as plt
import gold

with open('stocks.json', 'r') as f:
  STOCKS = json.load(f)

def width(stocks):
  return min(len(stocks), 3)
def height(stocks):
  if len(stocks) >= 3:
    return ceil(len(stocks)/3)
  return 1

# input(f'{width(STOCKS)}, {height(STOCKS)}')

fig, figs = plt.subplots(height(STOCKS), width(STOCKS))


for i, stock in enumerate(STOCKS):


  data = pdr.get_data_yahoo(stock)


  print(i)
  # print([x for x in data])
  # x = list(data)
  
  data = list(data['Close'])
  if stock == 'GC=F':
    data = [number*28.43685319317602 for number in data]
    figs[int((i)/width(STOCKS))][max(0,i)%width(STOCKS)].set_title(f'{stock} : {gold.get_price()}')
  else:
    figs[int((i)/width(STOCKS))][max(0,i)%width(STOCKS)].set_title(f'{stock} : {data[-1]}')
  print(data)
  figs[int((i)/width(STOCKS))][max(0,i)%width(STOCKS)].plot(data) #(STOCKS)
  

# plt.plot(data)
# plt.subplots_adjust(left=0.080, right=0.965, top=0.960, bottom=0.090)
# plt.savefig('stock.png') #, width=1920, height=1080)
plt.show()

# import ctypes
# import os
# input(os.path.abspath(os.getcwd()))
# ctypes.windll.user32.SystemParametersInfoW(20, 0,  os.path.abspath(os.getcwd())+'\\stock.png', 0)