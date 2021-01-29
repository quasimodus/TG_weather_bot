TOKEN = '1469485782:AAGri4fgnwXkWrt5sVp0HnYoKh3C-rtx6Zw'
URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 505372163

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    UPDATE_ID = file.readline()

CITY = 'Tula'
WEATHER_TOKEN = 'c20ea049a76d07a8d39defb5b25de0a3'
WEATHER_URL = f'api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_TOKEN}'