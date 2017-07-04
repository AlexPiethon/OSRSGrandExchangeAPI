import requests
import apiutil as util

OFFICIAL_BASE_URL = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='
RSBUDDY_BASE_URL = 'https://api.rsbuddy.com/grandExchange?a=guidePrice&i='

class API():
    def get_raw_dict(self, item_name):
        j_dict = util.query_item(item_name, self.base_url)
        if j_dict is None:
            print('Item: \'%s\' could not be found.' % item_name)
            return None
        return j_dict

    def get_prices(self, item_list):
        price_dict = {}
        for item in item_list:
            price = self.get_price(item)
            if price != 0:
                price_dict[item] = price
        return price_dict

class OfficialAPI(API):
    def __init__(self):
        self.base_url = OFFICIAL_BASE_URL

    def parse_price(self, value):
        if str(value).isdigit():
            return value

        if value[-1] == 'm':
            return int(float(value[:-1]) * 1000000)
        if value[-1] == 'k':
            return int(float(value[:-1]) * 1000)

        value = value.replace(',', '')
        return int(value)

    def get_price(self, item_name):
        j_dict = self.get_raw_dict(item_name)
        return self.parse_price(j_dict['item']['current']['price']) if j_dict != None else 0

    def get_image(self, item_name):
        j_dict = self.get_raw_dict(item_name)
        return j_dict['item']['icon_large'] if j_dict != None else 0

    def get_daily_price_dict(self, item_name):
        URL = 'http://services.runescape.com/m=itemdb_oldschool/api/graph/'
        item_id = util.get_id(item_name)
        if item_id is None:
            print('Item: \'%s\' could not be found.' % item_name)
            return None
        req_url = URL + str(item_id) + '.json'
        r = requests.get(req_url)
        return r.json()


class RSBuddyAPI(API):
    def __init__(self):
        self.base_url = RSBUDDY_BASE_URL

    def get_price(self, item_name):
        j_dict = self.get_raw_dict(item_name)
        return int(j_dict['overall']) if j_dict != None else 0
