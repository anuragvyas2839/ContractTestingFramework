import requests

from static_data import url_endpoints

url_mapping = url_endpoints.api_endpoints
base_url = url_endpoints.base_url


def get_endpoint_url(endpoint):
    '''Util function to return complete url by endpoint'''
    return base_url + url_mapping[endpoint]


def get_response_for_get_request(url, header={'Content-Type': 'application/json'}, params=None, auth=None):
    '''Util function to go a get request and return the response'''
    return requests.get(url=url, headers=header, params=params, auth=auth)


def get_response_for_post_request(url, header={'Content-Type': 'application/json'}, params=None, json=None, auth=None):
    '''Util function to go a post request and return the response'''
    return requests.post(url=url, headers=header, params=params, json=json, auth=auth)
