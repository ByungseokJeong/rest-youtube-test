import requests

url = "http://localhost:8000/api/auth"

response = requests.post(url, data = {'username' : 'admin', 'password' : '123123'})

print(response.text)

myToken = response.json()

print(myToken['token'])
token = myToken['token']
header = {'Authorization' : 'Token 836a9d9b2ec051373241a3aa6698686910ead64c'}
response = requests.get('http://localhost:8000/api/student_list ', headers=header)
print(response.text)

