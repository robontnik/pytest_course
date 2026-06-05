import httpx
from tools.fakers import get_random_email

create_payload = {
  "email": get_random_email(),
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


create_file_headers = {
    'Authorization' : f'Bearer {login_response_data['token']['accessToken']}'
}

create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    data = {'filename' : 'image.jpg', 'directory' : 'courses'},
    files = {"upload_file" : open('./testdata/files/image.jpg', 'rb')},
    headers= create_file_headers 
    )

create_file_response_json = create_file_response.json()
print("Create file data:", create_file_response_json)