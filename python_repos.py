import requests

# Make an API call and store the response.

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
# Makes the API call.
# Call get and pass it the URL and the header that we defined and we assign the response object to the variable r.
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
# API returns the info in JSON format, so we use the json method to convert the info to a python dictionary.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Process results
repo_dicts = response_dict['items']
print(f"Repos returned: {len(repo_dicts)}")

print("\nSelected information about each repo:")
for repo_dict in repo_dicts:
    #repo_dict = repo_dicts[0]
    #print("\nSelected info about first repo:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repos: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
#print(f"\nKeys: {len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
    #print(key)
