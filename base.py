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
        # if len(users) > 3200:
        #     break
        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            break
    return users

# starred_users = get_starred_users("<repo-name>", "<access-token>")

with open("./.tokens.json", "r") as file1:
    tokens = json.load(file1)
    github_access_token = tokens["github_access_token"]
    print(github_access_token)
    repo_name = "jojocys/FGHU-Game"
    save_file_name = repo_name.replace("/", "_")
    with open(f"./data/starred_users_{save_file_name}.json", "w") as file2:
        starred_users = get_starred_users(repo_name, github_access_token)
        json.dump(starred_users, file2)