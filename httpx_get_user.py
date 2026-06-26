import httpx
from tools.fakers import fake

create_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_payload)
create_response_data = create_response.json()
print('Create user response:' , create_response_data)


login_payload = {
    "email": create_payload['email'],
    "password": create_payload['password']
}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print('Login response:' , login_response_data)



get_response = httpx.get(f'http://127.0.0.1:8000/api/v1/users/{create_response_data['user']['id']}', headers = {'Authorization' : f'Bearer {login_response_data['token']['accessToken']}'})
get_response_data = get_response.json()
print('Get user response:' , get_response_data)