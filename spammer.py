import requests
url = input("Enter discord Webhook link:\n")
message = input("Enter message:\n")

while True:
    count = input("Enter number of messages to be sent:\n")
    data = {
        "content": message
    }
    if count.isalnum():
        for i in range(int(count)):
            requests.post(url, data=data)
        print("\nSpammed! Thank you for using this program\n\nMade by Kiwifruit\n")
        input()
        break
    else:
        continue