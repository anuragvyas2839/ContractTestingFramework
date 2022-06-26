from pact import Like

from static_data.url_endpoints import api_endpoints


pact_block_params_list = [
    {
        'given': 'User with user id 2 exists in database table user_details',
        'upon_receiving': 'a request for get User2 details',
        'url': api_endpoints['get_user'].format(2),
        'expected': {
            'status_code': 200,
            'data': Like({
                "data": {
                    "id": 2,
                    "email": "janet.weaver@reqres.in",
                    "first_name": "Janet",
                    "last_name": "Weaver",
                    "avatar": "https://reqres.in/img/faces/2-image.jpg"
                },
                "support": {
                    "url": "https://reqres.in/#support-heading",
                    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
                }
            }),
            'query_params': None,
            'request_body': None,
        },
    },
    {
        'given': 'Provider only allows int user ids',
        'upon_receiving': 'a request for get user with string as user id',
        'url': api_endpoints['get_user'].format('abcd'),
        'expected': {
            'status_code': 400,
            'data': {},
            'query_params': None,
            'request_body': None,
        },
    },
]
