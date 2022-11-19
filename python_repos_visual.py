import requests

from plotly.graph_objs import Bar
from plotly import offline

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
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make visualizations.
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
        'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repoistory',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

