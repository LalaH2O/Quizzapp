import functs
import requests
from settings import debug, api_folder

print('Admin console activated')
print('checking indernet...')
print('Google answered with status code: ' + str(requests.get(url = 'https://google.com').status_code))
print('200 means OK')
print('please continiue')
input = input('select mode: ')

if input == 'clear_all':
    ids = requests.get(url=api_folder + 'transalator.php', params={'download_list':True}).text
else:
    print('bad input')