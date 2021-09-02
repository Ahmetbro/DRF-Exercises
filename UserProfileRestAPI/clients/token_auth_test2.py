import requests

from pprint import pprint


# {'key': '6dc6677835b5e9c9d22c0f5c4b2825144709c54e'}
def client():

    token = 'Token 2c7126d05611a4b57324197b8be79b4b32ed3865'
    headers = {
        'Authorization': token,
    }
    response = requests.get(
        url= 'http://127.0.0.1:8000/api/user-profiles/',
        headers=headers
    )

    print('status code:', response.status_code)
    
    response_data = response.json()

    pprint(response_data)


if __name__ == '__main__':
    client()