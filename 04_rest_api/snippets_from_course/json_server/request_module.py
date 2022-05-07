import requests


# TODO: Basic info from server
reply = requests.get('http://localhost:3000')
print(reply.status_code)
print(requests.codes.__dict__)
if reply.status_code == requests.codes.ok:
    print("Ok")
print(reply.headers)
print(reply.headers['Content-Type'])
print(reply.text)


# TODO: Timeout get()
# try:
#     reply = requests.get('http://localhost:3000', timeout=1)
# except requests.exceptions.Timeout:
#     print('Sorry, Mr. Impatient, you did not get your data')
# else:
#     print('Here is your data, my Master!')


# TODO: Timeout connection
# try:
#     reply = requests.get('http://localhost:3001', timeout=1)
# except requests.exceptions.ConnectionError:
#     print('Nobody\'s home, sorry!')
# else:
#     print('Everything fine!')


# TODO: Invalid URL
# try:
#     reply = requests.get('http:////////////')
# except requests.exceptions.InvalidURL:
#     print('Recipient unknown!')
# else:
#     print('Everything fine!')
