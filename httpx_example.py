import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/200')

print(response.status_code)
print(response.json())


data = {
    'title': 'foo',
    'completed': False,
    'userId': 1
}

response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data) 
print(response.status_code)
print(response.json())

data = {
    'username': 'foo',     
    'password': 'bar'
}

response = httpx.post('https://httpbin.org/post', data=data)
print(response.status_code)
print(response.json())

headers = {
    'Authorization': 'Bearer your_token_here'}

response = httpx.get('https://httpbin.org/get', headers=headers)
print(response.request.headers)
print(response.json())


params = {
    'userId': 1
    }

response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
print(response.url)
print(response.json())


files = {
    'file': ('example.txt', open('example.txt', 'rb'))
    }

response = httpx.post('https://httpbin.org/post', files=files)
print(response.status_code)
print(response.json())


with httpx.Client() as client:
    response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
    response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')

print(response1.status_code)
print(response1.json())
print(response2.status_code)
print(response2.json())

client = httpx.Client(headers={'Authorization':'Bearer your_token_here'})

response = client.get('https://httpbin.org/get')
print(response.json())

try:
    response = httpx.get('https://jsonplaceholder.typicode.com/invalid')
    response.raise_for_status()
except httpx.HTTPStatusError as exc:
    print(f'Error response {exc.response.status_code} while requesting {exc.request.url!r}.')


try:
    response = httpx.get('https://httpbin.org/delay/5', timeout=2.0)
except httpx.ReadTimeout as exc:
    print(f'Timeout while requesting {exc.request.url!r}.')