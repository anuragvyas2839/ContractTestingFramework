import atexit
import unittest
from pact import Consumer, Provider
from pact.matchers import get_generated_values

from pact_block_params import display_user_calls_get_user_params
from utils.mock_service_calls import user_mock_service_calls

pact = Consumer('DisplayUserConsumer').has_pact_with(Provider('GetUserProvider'))
pact.start_service()
atexit.register(pact.stop_service)


class GetUserInfoContract(unittest.TestCase):

    def test_get_user_pacts(self):
        '''Method to publish pact interactions for contract of get users api called from display users'''
        for block_params in display_user_calls_get_user_params.pact_block_params_list:
            expected = block_params['expected']
            url = block_params['url']
            (pact
             .given(block_params['given'])
             .upon_receiving(block_params['upon_receiving'])
             .with_request('get', url)
             .will_respond_with(expected['status_code'], body=expected['data'])
             )
            with pact:
                result = user_mock_service_calls.get_user(url)
            self.assertEqual(result.status_code, expected['status_code'])
            self.assertEqual(result.json(), get_generated_values(expected['data']))
