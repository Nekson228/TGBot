import requests
import json
import sys

cc = '7'
phone = '9024925012'
RED = '\033[31m'
ENDC = '\033[0m'


def get_response(url, method: str, headers: dict = None, parameters: dict = None, data: dict = None):
    try:
        response = requests.request(method, url, headers=headers, params=parameters, data=data)
        if response.status_code == 200:
            return response
        print(f'{RED}{response.status_code}{ENDC}')
        return None
    except requests.exceptions.ConnectionError:
        print(f'{RED}No internet connetion.{ENDC}')
        sys.exit()


with open('apidata.json', 'r') as file:
    reqs = json.load(file)

for new_req in reqs['sms']['multi']:
    params = new_req.get('params', None)
    headers = new_req.get('headers', None)

    data_req = new_req.get('data', None)
    if data_req:
        data_req[list(data_req.keys())[0]] = data_req[list(data_req.keys())[0]].format(cc=cc, target=phone)

    print(new_req['method'], new_req['url'], params, data_req)
    response = get_response(new_req['url'], new_req['method'], parameters=params, data=data_req, headers=headers)
    print(response if response else f"{RED}Got no response :({ENDC}")