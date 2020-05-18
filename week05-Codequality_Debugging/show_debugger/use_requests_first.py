import requests

auth_header = {'Authorization': 'token {}'.format(usernamepw.ACCESSTOKEN)}
print(requests.get('https://api.github.com/orgs/scientificprogramminguos/repos', headers=auth_header))