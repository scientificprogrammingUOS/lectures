from util.request_wrapper_original import requests
import usernamepw

def main():
    some_func()

def some_func():
    auth_header = {'Authorization': 'token {}'.format(usernamepw.ACCESSTOKEN)}
    a = requests.get('https://api.github.com/orgs/scientificprogramminguos/repos', headers=auth_header)
    ratelimit = int(a.headers._store['x-ratelimit-remaining'][1])
    print("rate-limit:", ratelimit)


if __name__ == '__main__':
    b = 2
    main()