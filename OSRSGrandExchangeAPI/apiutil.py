import requests
import json

with open('items.json') as items_file:
    items = json.loads(items_file.read())

for item in items:
    item['id'] = int(item['id'])
    item['name'] = item['name'].encode('ascii', 'replace')

def get_id(name):
    for item in items:
        if name.lower() == item[u'name'].lower():
            return int(item['id'])
    return None

def query_item(name, base):
    item_id = get_id(name)
    if item_id is None:
        return None
    r = requests.get(base+str(item_id))
    return r.json()

# Expects a string
def parse_price(value):
    if str(value).isdigit():
        return value

    value = value.replace(',', '')

    if value[-1] == 'm':
        return int(float(value[:-1]) * 1000000)

    if value[-1] == 'k':
        return int(float(value[:-1]) * 1000)

    return int(value)
