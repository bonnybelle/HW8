# -*- coding: utf-8 -*-

import random
import requests

try_amount = int(input('Число попыток: '))
RCODES = [200, 300, 403, 404, 500]
# '200 - Success', '300 - Redirection', '403, 404 - Client Errors', '500 - Server Errors'
URL = 'https://httpbin.org/status/{st}'


def retry(try_count):
    def create_retry(func):
        def wrapper(*args):
            for i in range(try_count):
                if func(*args) == 200:
                    return 'OK'

            return 'ERROR'

        return wrapper

    return create_retry


@retry(try_amount)
def get_request():
    code = random.choice(RCODES)
    print(code)
    resp = requests.get(URL.format(st=code))
    return resp.status_code


print(get_request())
exit()

# def retry_deco(func):
#    def wrapper(lst):
#        # for x in lst:
#        ...

#    return


# @retry_deco


# print(read_x(x = int(input())))
'''
if __name__ == '__main__':
    numbers = read_x()
'''
