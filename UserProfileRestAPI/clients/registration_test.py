import requests

from pprint import pprint


# {'key': '6dc6677835b5e9c9d22c0f5c4b2825144709c54e'}
def client():
    credentials = {
        'username': 'rest_TestUser2',
        'email' : 'test@test.co',
        'password1': 'testing123...',
        'password2': 'testing123...',
    }

    response = requests.post(
        url= 'http://127.0.0.1:8000/api/rest-auth/registration/',
        data= credentials,
    )

    print('status code:', response.status_code)
    
    response_data = response.json()

    pprint(response_data)


if __name__ == '__main__':
    client()