import requests

TOKEN = '1469485782:AAGri4fgnwXkWrt5sVp0HnYoKh3C-rtx6Zw'
URL = 'https://api.telegram.org/bot{TOKEN}/{method}'
updates = 'getUpdates'
send = 'sendMessage'

data = {
    'chat_id': '505372163',
    'text': 'Hello from Test_bot'
}
url = URL.format(TOKEN=TOKEN, method=send)
response = requests.post(url, data=data)

print(response.text)

