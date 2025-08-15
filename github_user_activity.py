import requests
import json

github_username = input("Github username: ")

r = requests.get(f"https://api.github.com/users/{github_username}/events")
json_file = r.json()

print(json_file.)
