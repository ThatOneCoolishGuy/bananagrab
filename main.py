import time
import requests
print("Welcome to BananaGrab!")
time.sleep(1)
t = input("Please enter the URL of the website to fetch. - ")
time.sleep(1)
r = requests.get(t)
print(r.text)
