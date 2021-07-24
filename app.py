
# Importing libraries
from binance.client import Client
from binance.streams import ThreadedWebsocketManager
import time
##############################################################################
# Loading keys from config file
ACTUAL_API_KEY  ='myapi'
ACTUAL_SECRET_KEY = 'myapisecret'

# Setting up connection
client = Client(ACTUAL_API_KEY, ACTUAL_SECRET_KEY)
#client.API_URL = 'https://testnet.binance.vision/api'  # To change endpoint URL for test account
# Getting account info to check balance
info = client.get_account()  # Getting account info   
# Saving different tokens and respective quantities into lists
assets = []
values = []
for index in range(len(info['balances'])):
for key in info['balances'][index]:
if key == 'asset':
assets.append(info['balances'][index][key])
if key == 'free':
values.append(info['balances'][index][key])

token_usdt = {}  # Dict to hold pair price in USDT
token_pairs = []  # List to hold different token pairs
# Creating token pairs and saving into a list
for token in assets:
if token != 'USDT':
token_pairs.append(token + 'USDT')
def streaming_data_process(msg):
"""
    Function to process the received messages and add latest token pair price
    into the token_usdt dictionary
    :param msg: input message
    """
global token_usdt
token_usdt[msg['s']] = msg['c']

def total_amount_usdt(assets, values, token_usdt):
"""
    Function to calculate total portfolio value in USDT
    :param assets: Assets list
    :param values: Assets quantity
    :param token_usdt: Token pair price dict
    :return: total value in USDT
    """
total_amount = 0
for i, token in enumerate(assets):
if token != 'USDT':
total_amount += float(values[i]) * float(
token_usdt[token + 'USDT'])
else:
total_amount += float(values[i]) * 1
return total_amount

def total_amount_btc(assets, values, token_usdt):
"""
    Function to calculate total portfolio value in BTC
    :param assets: Assets list
    :param values: Assets quantity
    :param token_usdt: Token pair price dict
    :return: total value in BTC
    """
total_amount = 0
for i, token in enumerate(assets):
if token != 'BTC' and token != 'USDT':
total_amount += float(values[i]) \
                            * float(token_usdt[token + 'USDT']) \
                            / float(token_usdt['BTCUSDT'])
if token == 'BTC':
total_amount += float(values[i]) * 1
else:
total_amount += float(values[i]) \
                            / float(token_usdt['BTCUSDT'])

return total_amount

def assets_usdt(assets, values, token_usdt):
"""
    Function to convert all assets into equivalent USDT value
    :param assets: Assets list
    :param values: Assets quantity
    :param token_usdt: Token pair price dict
    :return: list of asset values in USDT
    """
assets_in_usdt = []
for i, token in enumerate(assets):
if token != 'USDT':
assets_in_usdt.append(
float(values[i]) * float(token_usdt[token + 'USDT'])

            )
else:
assets_in_usdt.append(float(values[i]) * 1)

print(assets_in_usdt)           
return assets_in_usdt
