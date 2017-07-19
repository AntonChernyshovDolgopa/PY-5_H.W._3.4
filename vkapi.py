import requests
import urllib3
import pprint
import json
from urllib.parse import urlencode

authorize_url = 'https://oauth.vk.com/authorize'
app_id = 6119543
service_access_key = '2e2c41e42e2c41e42e2c41e4d32e71219322e2c2e2c41e47743dec51cb467606196ad3e'
secure_key = 'Avp0FH8gxU7InqQzbuUH'
version = '5.67'


auth_data = {
    'client_id' : app_id,
    'redirect_uri' : 'https://oauth.vk.com/blank.html',
    'display' : 'popup',
    'scope' : 'friends, status',
    'response_type' : 'token',
    'v' : version
}

print ('?'.join(
    (authorize_url, urlencode(auth_data))
))

access_token = 'fd6a129fdddadd66668232a7bfff113332700971c41f1f52f0b0683d22b8f8a2824411e73ec5504d596ae'
expires_in = 86400
user_id = 1848608

params_1 = {
    'access_token' : access_token,
    'v' : version,
    'fields' : 'nickname'
}

# список всех моих друзей
response_1 = requests.get('https://api.vk.com/method/friends.get', params_1)
#print(response_1.json())

params_2 = {
    'access_token' : access_token,
    'v' : version,
    'source_uid' : user_id,
    'target_uid' : 24094
}
response_2 = requests.get('https://api.vk.com/method/friends.getMutual', params_2)
print(response_2.json())