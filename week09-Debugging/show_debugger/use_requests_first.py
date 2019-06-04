import requests

auth_header = {'Authorization': 'token {}'.format('fe818da94cdf5710cbaad5d1234670be670fbf9d')}
requests.get('https://api.github.com/orgs/scientificprogramminguos/repos', headers=auth_header).json()