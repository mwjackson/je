from pprint import pformat, pprint

import requests
import json


def query_outcode(code):
    """
    pretty prints a list of restaurants for a given outcode, sorted by rating desc
    :param code: the outcode to search by
    :return: the data (for testing)
    """
    resp = _get_request(code)

    restaurants = _map_response(resp.text)

    print _format_data(restaurants)

    return restaurants


def _get_request(code):
    """
    perform the get using requests
    :param code: the code to include in the querystring
    :return: response object
    """
    
    return requests.get('https://public.je-apis.com/restaurants?q={0}'.format((code or '').lower()), headers={
        'accept-tenant': 'uk',
        'accept-language': 'en-GB',
        'authorization': 'Basic VGVjaFRlc3RBUEk6dXNlcjI=',
        'host': 'public.je-apis.com'
    })


def _map_response(data):
    """
    map the text to a dict via json and select the relevant keys
    :param data:
    :return: a dict of the data
    """

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
    """
    format the data in a tabular fashion
    :param data:
    :return:
    """

    header = 'Name'.ljust(50) + 'Rating'.ljust(20) + 'Cuisines'
    return u'\n'.join(['', header] +
                     [r['Name'].ljust(50) + str(r['RatingAverage']).ljust(20) + ', '.join(r.get('CuisineTypes', [])) for r in data])