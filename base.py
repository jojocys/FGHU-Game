import requests
import json

def get_starred_users(repo_name, access_token):
    headers = {
        "Authorization": f"Token {access_token}"
    }
    users = []
    url = f"https://api.github.com/repos/{repo_name}/stargazers"
    while True:
        response = requests.get(url, headers=headers)
        data = response.json()
        users.extend(data)
        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            break
    return users

starred_users = get_starred_users("<repo-name>", "<access-token>")

with open("starred_users.json", "w") as file:
    json.dump(starred_users, file)