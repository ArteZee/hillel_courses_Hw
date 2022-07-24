import datetime

import requests

url_currency_today = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode="

now = datetime.datetime.now()
today_data = now.strftime("%Y%m%d")
# get user data
user_data: str = input("Put currency or specific date if u do not put date will be today`s\n"
                       "(Date in format yyyy mm dd) : ").upper()
user_data_1: list = user_data.split(" ")

# if user get only currency - date paste today
if len(user_data_1) == 1:
    complete_url = url_currency_today + user_data_1[0] + "&date=" + today_data + "&json"
# if user put currency and date - paste it in url
else:
    complete_url = url_currency_today + user_data_1[0] + "&date=" + "".join(user_data_1[1:]) + "&json"
# if currency in jason file
if user_data_1[0] in r_data[0].values():
    print(r_data[0]["cc"], "-", r_data[0]["rate"])
#  if user put incorrect format time
elif r_data[0]['message'] == 'Wrong parameters format':
    print("Invalid date {}".format(' '.join(user_data_1[1:])))
# if currency doesn't match
elif not r_data:
    print("Invalid currency name: {}".format(user_data_1[0]))
