
import time
import requests

print("start")
time.sleep(2)
print("finish")

response = requests.get("http://www.example.com")
print(response.content)

