import requests


def query_outcode(code):
    pass


def _get_request(code):
    return requests.get('https://public.je-apis.com/restaurants?q={0}'.format((code or '').lower()), headers={
        'accept-tenant': 'uk',
        'accept-language': 'en-GB',
        'authorization': 'Basic VGVjaFRlc3RBUEk6dXNlcjI=',
        'host': 'public.je-apis.com'
    })