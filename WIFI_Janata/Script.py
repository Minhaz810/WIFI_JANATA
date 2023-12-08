# import os
# import django
# import json
# from datetime import datetime
# if __name__ == '__main__':
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Janata_WIFI.settings")
#     django.setup()

# from Dynamic_Table.models import JWData

# json_file_path = 'static/json/stock_market_data.json'
# with open(json_file_path, 'r') as json_file:
    
#     json_data = json.load(json_file)


# for item in json_data:
#     JWData.objects.create(
#         Date=datetime.strptime(item['date'], '%Y-%m-%d').date(),
#         TradeCode=(item['trade_code']),
#         High=float(item['high'].replace(',','')),
#         Low=float(item['low'].replace(',','')),
#         Open=float(item['open'].replace(',','')),
#         Close=float(item['close'].replace(',','')),
#         Volume=int(item['volume'].replace(',',''))
#     )
      
