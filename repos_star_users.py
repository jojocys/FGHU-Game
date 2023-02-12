import requests
import json

def get_starred_repos(username, access_token):
    headers = {
        "Authorization": f"Token {access_token}"
    }
    repos = []
    url = f"https://api.github.com/users/{username}/starred"
    while True:
        response = requests.get(url)
        data = response.json()
        repos.extend(data)
        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            break
    return repos

username = "<github-username>"
starred_repos = get_starred_repos(username)

with open(f"./data/starred_repos_{username}.json", "w") as file:
    json.dump(starred_repos, file)
