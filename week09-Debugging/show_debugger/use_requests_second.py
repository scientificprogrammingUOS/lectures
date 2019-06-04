import requests
import usernamepw

#curl -i -X 'GET' -H 'Authorization: token fe818da94cdf5710cbaad5d1234670be670fbf9d' 'https://api.github.com/orgs/scientificprogramminguos/repos'

def main():
    auth_header = {'Authorization': 'token {}'.format(usernamepw.ACCESSTOKEN)}
    resp = requests.get('https://api.github.com/orgs/scientificprogramminguos/repos', headers=auth_header)
    print()

if __name__ == '__main__':
    main()