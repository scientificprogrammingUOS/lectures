import requests as imported_requests
import time
import traceback
from datetime import datetime


time_from_headers = lambda x: datetime.utcfromtimestamp(int(x['x-ratelimit-reset'])+2*60*60).strftime('%Y-%m-%d %H:%M:%S')


class RequestWrapper():
    def __init__(self):
        self.num_gets = 0
        self.num_puts = 0
        self.num_posts= 0


    def inc(self, what):
        if what == 'get':
            self.num_gets += 1
        elif what == 'post':
            self.num_posts += 1
        elif what == 'put':
            self.num_puts += 1
        if self.num_calls % 50 == 1:
            print()


    @property
    def num_calls(self):
        return self.num_gets+self.num_posts+self.num_puts


    def get(self, *args, **kwargs):
        resp = imported_requests.get(*args, **kwargs)
        self.check_xrate_limit(resp)
        self.inc('get')
        return resp

    def post(self, *args, **kwargs):
        resp = imported_requests.post(*args, **kwargs)
        self.check_xrate_limit(resp)
        self.inc('post')
        return resp

    def put(self, *args, **kwargs):
        resp = imported_requests.put(*args, **kwargs)
        self.check_xrate_limit(resp)
        self.inc('put')
        return resp


    def check_xrate_limit(self, resp):
        try:
            headers = {key: value[1] for key, value in dict(resp.headers._store).items()}
            if not 'x-ratelimit-remaining' in headers:
                return
            if int(headers['x-ratelimit-remaining']) == 0:
                # print("!!! API-Limit reached! Reset at", time_from_headers(headers), "!!!")
                import sys; sys.exit(1)
            elif (int(headers['x-ratelimit-remaining']) < 50 and int(headers['x-ratelimit-remaining']) % 10 == 0) or self.num_calls==0:
                print("API-Calls left:", headers['x-ratelimit-remaining'])
            if int(headers['x-ratelimit-remaining']) < 5:
                # print("No API-Calls left! Gonna sleep until", time_from_headers(headers))
                sleeptime = (datetime.utcfromtimestamp(int(headers['x-ratelimit-reset'])+2*60*60)- datetime.now()).seconds
                time.sleep(sleeptime+5)
                self.num_puts = self.num_posts = self.num_gets = 0
        except Exception as e:
            traceback.print_exc()
            print()


requests = RequestWrapper()