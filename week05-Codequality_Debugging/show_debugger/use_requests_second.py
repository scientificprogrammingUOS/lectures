import requests
import usernamepw

#curl -i -X 'GET' -H 'Authorization: token THE_TOKEN' 'https://api.github.com/orgs/scientificprogramminguos/repos'

def main():
    auth_header = {'Authorization': 'token {}'.format(usernamepw.ACCESSTOKEN)}
    resp = requests.get('https://api.github.com/orgs/scientificprogramminguos/repos', headers=auth_header)
    print()

if __name__ == '__main__':
    main()