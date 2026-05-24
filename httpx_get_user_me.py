import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print('Login response:' , login_response_data)
print('Status code:',login_response.status_code)

get_user_response = httpx.get('http://localhost:8000/api/v1/users/me', headers= {'Authorization' : f"Bearer {login_response_data['token']['accessToken']}"})
print('Get user response:' , get_user_response.json())
print('Status code:',get_user_response.status_code)