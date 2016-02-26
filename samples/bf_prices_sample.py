import OSRSGrandExchangeAPI as api
import sys

oapi = api.OfficialAPI()

rsbapi = api.RSBuddyAPI()

raw = ['coal', 'iron ore', 'mithril ore', 'adamantite ore', 'runite ore']
finished = ['steel bar', 'mithril bar', 'adamantite bar', 'runite bar']

oraw_prices = oapi.get_prices(raw)
ofinished_prices = oapi.get_prices(finished)

rraw_prices = rsbapi.get_prices(raw)
rfinished_prices = rsbapi.get_prices(finished)

oprofits = {'steel bar': ofinished_prices['steel bar'] - (oraw_prices['iron ore'] + oraw_prices['coal']),
          'mithril bar': ofinished_prices['mithril bar'] - (oraw_prices['mithril ore'] + 2*oraw_prices['coal']),
          'adamantite bar': ofinished_prices['adamantite bar'] - (oraw_prices['adamantite ore'] + 3*oraw_prices['coal']),
          'runite bar': ofinished_prices['runite bar'] - (oraw_prices['runite ore'] + 4*oraw_prices['coal'])
}

rprofits = {'steel bar': rfinished_prices['steel bar'] - (rraw_prices['iron ore'] + rraw_prices['coal']),
          'mithril bar': rfinished_prices['mithril bar'] - (rraw_prices['mithril ore'] + 2*rraw_prices['coal']),
          'adamantite bar': rfinished_prices['adamantite bar'] - (rraw_prices['adamantite ore'] + 3*rraw_prices['coal']),
          'runite bar': rfinished_prices['runite bar'] - (rraw_prices['runite ore'] + 4*rraw_prices['coal'])
}


print 'Based on official prices: ', oprofits
print 'Based on OSBuddy prices: ', rprofits
