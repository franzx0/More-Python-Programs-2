import requests

url = "https://api.github.com/search/repositories?q=stars:>10000&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

response_dict = response.json()
repo_dicts = response_dict["items"]
print(f"Total repositories returned: {len(repo_dicts)}")

for repo_dict in repo_dicts[:10]:
    print("\nSelected information about each repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
