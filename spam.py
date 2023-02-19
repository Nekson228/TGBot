import requests
import json
import sys

cc = '7'
target = '9825744661'
YELLOW = '\033[33m'
ENDC = '\033[0m'

format_types = {
    "default": (lambda x: x),
    "+default": (lambda x: f"+{x}"),
    "normalized": (lambda x: f"+{x[0]} ({x[1:4]}) {x[4:7]}-{x[7:9]}-{x[9:]}"),
}


def get_response(url, method: str, headers: dict = None, parameters: dict = None, data: dict = None):
    try:
        response = requests.request(method, url, headers=headers, params=parameters, data=data)
        if response.status_code == 200:
            return response
        print(f'{YELLOW}{response.status_code}{ENDC}')
        return None
    except requests.exceptions.ConnectionError:
        print(f'{YELLOW}No internet connetion.{ENDC}')
        sys.exit()


def fill_in_phone_data(request: dict):
    path, formatting = request.get('path', None), request.get('format', None)
    if not path or not formatting:
        print(f"{YELLOW}Идиот, ты не заполнил {request['name']} :/{ENDC}")
        return
    if 'all' in path:
        formatting = format_types[formatting] if formatting in format_types else eval(formatting)
        phone = formatting(f'{cc}{target}')
        exec(f'request{path["all"]} = "{phone}"')


with open('apidata.json', 'r') as file:
    reqs = json.load(file)

for new_req in reqs['sms']['multi']:
    fill_in_phone_data(new_req)
    params = new_req.get('params', None)
    headers = new_req.get('headers', None)
    data_req = new_req.get('data', None)

    print(new_req['name'], new_req['method'], new_req['url'], params, data_req)
    response = get_response(new_req['url'], new_req['method'], parameters=params, data=data_req, headers=headers)
    print(response if response else f"{YELLOW}Got no response :({ENDC}")
