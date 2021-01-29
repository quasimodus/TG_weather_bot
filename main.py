import requests
import json
import time
from pprint import pprint
import const


def get_weather(location):
    url = const.WEATHER_URL.format(city=location, token=const.WEATHER_TOKEN)
    response = requests.get(url)
    print(response.content)


def get_message(data):
    return data['message']['text']




def save_update_id(update):
    with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    return True


def main():
    while True:
        url = const.URL.format(token=const.TOKEN, method=const.UPDATE_METH)
        content = requests.get(url).text

        data = json.loads(content)
        result = data['result'][::-1]
        needed_part = None

        for elem in result:
            if elem['message']['chat']['id'] == const.MY_ID:
                needed_part = elem
                print(needed_part)
                break

        if const.UPDATE_ID != needed_part['update_id']:
            message = get_message(needed_part)
            #get_message(needed_part)
            get_weather(message)

            print(const.UPDATE_ID)
            print(needed_part['update_id'])

            save_update_id(needed_part)

        # pprint(needed_part)

        # pprint(data)
        break
        time.sleep(2)


if __name__ == '__main__':
    main()
