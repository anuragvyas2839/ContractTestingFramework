from utils import request_response_utils
from static_data import url_endpoints


def get_user(endpoint_url):
    """Fetch a user object by user id from the server."""
    url = url_endpoints.base_url + endpoint_url
    return request_response_utils.get_response_for_get_request(url=url)
