import requests
url = input("Enter discord Webhook link:\n")
while True:
    message = input("Enter message:\n")
    data = {
        "content": message
    }
    requests.post(url, data=data)