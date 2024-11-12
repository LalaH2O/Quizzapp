import requests

#basics

help = 'Nothing to help'

debug = 0  # Set debug flag to 1 for debugging
api_folder = 'https://lassehelbling.ch/api/transalator/'

try:
    requests.get(url = api_folder, timeout=5).status_code
    online = 1
except requests.ConnectionError:
    online = 0

#Tkinter settings
proces_name = 'laca'
gui_bg_color = 'gray'
button_bg_color = 'gray'
button_text_color = 'white'
gui_font = 'helvetica'
gui_text_color = 'black'
window_position_x = '1000'
window_position_y = '300'

#functions
if debug == 1:
    print('Debug Enabled')