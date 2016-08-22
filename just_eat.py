from pprint import pformat, pprint

import requests
import json


def query_outcode(code):
    resp = _get_request(code)

    restaurants = _map_response(resp.text)

    print _format_data(restaurants)

    return restaurants


def _get_request(code):
    return requests.get('https://public.je-apis.com/restaurants?q={0}'.format((code or '').lower()), headers={
        'accept-tenant': 'uk',
        'accept-language': 'en-GB',
        'authorization': 'Basic VGVjaFRlc3RBUEk6dXNlcjI=',
        'host': 'public.je-apis.com'
    })


def _map_response(data):
    data = json.loads(data)

    restaurants = data.get('Restaurants', [])
    restaurants = [{k: r.get(k, '') for k in ['Name', 'CuisineTypes', 'RatingAverage']} for r in restaurants]
    restaurants = [_map_cuisine(r) for r in restaurants]
    restaurants = sorted(restaurants, key=lambda x: x.get('RatingAverage'), reverse=True)

    return restaurants


def _map_cuisine(r):
    r['CuisineTypes'] = [d['Name'] for d in r.get('CuisineTypes')]
    return r


def _format_data(data):
    header = 'Name'.ljust(50) + 'Rating'.ljust(20) + 'Cuisines'
    return u'\n'.join(['', header] +
                     [r['Name'].ljust(50) + str(r['RatingAverage']).ljust(20) + ', '.join(r.get('CuisineTypes', [])) for r in data])