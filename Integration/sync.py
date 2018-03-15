import requests
"""
Domain and Port should be set to the other project's 
environment that we send data to.

"""
PORT = ':9000'          # this Should be Changed
OTHER_HOST = '127.0.0.1'    # this Should be changed
BASE_URL = 'http://'+OTHER_HOST+PORT+'/api/'


def sync_db(obj, command):
    if command == 'POST':
        data = obj.__dict__
        r = requests.post(BASE_URL, data=data)
        print(r.status_code, r.reason)
    else:
        data = obj.__dict__
        detail_url = BASE_URL + str(obj.custom_key) + '/'
        if command == 'PUT':
            requests.put(detail_url, data=data)
        elif command == 'DELETE':
            r = requests.delete(detail_url)
            print(r.status_code, r.reason)
