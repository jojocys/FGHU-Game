import requests
import json

def get_repos(username, access_token, type_of_repo):
    headers = {
        "Authorization": f"Token {access_token}"
    }
    repos = []
    url = f"https://api.github.com/users/{username}/{type_of_repo}"
    while True:
        response = requests.get(url, headers=headers)
        data = response.json()
        repos.extend(data)
        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            break
    return repos

def get_starred_repos(username, access_token):
    return get_repos(username, access_token, "starred")

def get_forked_repos(username, access_token):
    return get_repos(username, access_token, "repos")

starred_repos = get_starred_repos("<github-username>", "<access-token>")
forked_repos = get_forked_repos("<github-username>", "<access-token>")

with open("starred_repos.json", "w") as file:
    json.dump(starred_repos, file)

with open("forked_repos.json", "w") as file:
    json.dump(forked_repos, file)
