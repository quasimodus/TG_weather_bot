TOKEN = '1469485782:AAGri4fgnwXkWrt5sVp0HnYoKh3C-rtx6Zw'
URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 505372163

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    UPDATE_ID = file.readline()


WEATHER_TOKEN = 'b1355580cc28d49e90ed35a90ef7172d'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
