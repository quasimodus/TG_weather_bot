import requests
import json
import time

import const


def main():
    while True:
        url = const.URL.format(token=const.TOKEN, method=const.UPDATE_METH)
        response = requests.get(url)
        print(response)
        time.sleep(2)


if __name__ == '__main__':
    main()