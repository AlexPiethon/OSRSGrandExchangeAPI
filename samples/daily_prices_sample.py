import API as api


oapi = api.OfficialAPI()

print oapi.get_daily_price_dict('mithril ore')
