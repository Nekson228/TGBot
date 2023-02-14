import requests
import json
import sys

cc = '7'
phone = '9825744661'
RED = '\033[31m'
ENDC = '\033[0m'


def get_response(url, method: str, headers: dict = None, parameters: dict = None, data: dict = None):
    try:
        response = requests.request(method, url, headers=headers, params=parameters, data=data)
        if response.status_code == 200:
            return response
        elif response.status_code == 401:
            print(f'{RED}{response.text}{ENDC}')
        else:
            print(f'{RED}{response.status_code}{ENDC}')
    except requests.exceptions.ConnectionError:
        print(f'{RED}No internet connetion.{ENDC}')
    sys.exit()


reqs = json.load(open('apidata.json', 'r'))

for i in range(len(reqs['sms']['multi'])):
    new_req = reqs['sms']['multi'][i]
    params = new_req.get('param', None)

    data_req = new_req.get('data', None)
    if data_req:
        data_req[list(data_req.keys())[0]] = data_req[list(data_req.keys())[0]].format(cc=cc, target=phone)

    print(new_req['method'], new_req['url'], params, data_req)
    try:
        response = get_response(new_req['url'], new_req['method'], parameters=params, data=data_req)
    except:
        print('POHUY PLASHEM')
    print(response)