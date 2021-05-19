import urllib3
import json


def main():
    # login
    api_key = 'B302581F-227D-EB11-9430-00155D09A733'
    secret = 'b1459606f44eefd6c46a8b2a589e10ff719a30f5285b74c38a198772431f1490'

    http = urllib3.PoolManager()

    url_base = 'https://api.bcr.com.ar/v1.0/'
    headers = {
        'api_key': api_key,
        'secret': secret,
        'Content-Type': 'application/json'
    }

    response = http.request('POST', url_base + 'Login', headers=headers)
    print(response.data)
    # since here on, we already have the login done: ergo, we've the token to get the other methods
    json_data = json.loads(response.data)
    token = json_data['data']['token']

    GET_METHOD = 'Cotizacion'

    headers_get = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response_get = http.request('GET', url_base + GET_METHOD, headers=headers_get)
    print(response_get.data)

    json_data_get = json.loads(response_get.data)

    print(json_data_get)


if __name__ == '__main__':
    main()