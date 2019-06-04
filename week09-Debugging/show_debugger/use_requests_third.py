from util.request_wrapper import requests
import usernamepw
import json

def main():
    auth_header = {'Authorization': 'token {}'.format(usernamepw.ACCESSTOKEN)}
    # resp = requests.get('https://api.github.com/orgs/scientificprogramminguos/repos', headers=auth_header)
    with open('cache_file.json', 'r') as cache_file:
        content = json.load(cache_file)['repos']

    hws = ['homework0' + str(i) for i in range(1, 9)]
    homework_repos = {}
    for homework in hws:
        homework_repos[homework] = [i for i in content if i['name'].startswith('2019-' + homework)]
    print()

if __name__ == '__main__':
    main()