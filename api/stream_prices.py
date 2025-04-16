import json
import requests

import constants.defs as defs
from models.live_api_price import LiveApiPrice

STREAM_URL = F"https://stream-fxpractice.oanda.com/v3"

#class PriceStreamer(threading.Thread):
#    def __init__(self, shared_prices, price_lock: threading.Lock, price_events):
#        super().__init__()
#        self.pairs_list = shared_prices.keys()
#        self.price_lock = price_lock
#        self.shared_prices = shared_prices
#        self.log = LogWrapper("PriceStreamer")
#        print(self.pairs_list)


def run(self):

    params = dict(
        instruments = ','.join(pairs_list)
    )

    url = f"{STREAM_URL}/accounts/{defs.ACCOUNT_ID}/pricing/stream"

    resp = requests.get(url, params = params, headers = defs.SECURE_HEADER, stream = True)

    for price in resp.iter_lines():
        if price:
            decoded_price = json.loads(price.decode('utf-8'))
            #print(decoded_price)
            #print()
            if 'type' in decoded_price and decoded_price['type'] == 'PRICE':
                print(LiveApiPrice(decoded_price))
