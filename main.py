# APPLICATION PROGRAMMING INTERFACES
#   a set of commands, functions, protocols, and objects that programmers can use to create
#   software or interact with an external system
#   Your Program => API Request => External System
#   External System => API Response => Your Program

# API Endpoint - the location of the external system
#   ex: api.coinbase.com

# API Request - the bank teller for the API bank vault
#   GET request: getting a piece of data

# JSON - just the string of a dictionary, can be sent across the internet easily
#   once you receive the JSON, you can then convert it into a dictionary

import requests
from datetime import datetime

MY_LAT = 37.168280
MY_LONG = -113.681870

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
#
# # Response Codes
# #   100s - hold on
# #   200s - here you go
# #   300s - go away
# #   400s - you screwed up
# #   500s - the server screwed up
#
# # so you can print the error message
# response.raise_for_status()
# # converting to json
# data = response.json()
# longitude = data["iss_position"]['longitude']
# latitude = data["iss_position"]['latitude']
# iss_position = (longitude, latitude)
#
# print(iss_position)

# API Parameters - inputs that will return certain responses

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
print(sunrise)

time_now = datetime.now()

print(time_now.hour)
