from flexmock import flexmock
import ubersmith_client
from ub_object_client import UbObjectClient


# def test_client_list():
#     client_list = flexmock()
#     client_list.should_receive('list').and_return({
#         "1001": {
#             "city": "Troy",
#         }
#     })
#
#     backend = flexmock(client=client_list)
#
#     object_api = ubersmith_object_api.init(backend=backend)
#     returned_object = object_api.client.list()
#
#     assert "Troy" == returned_object[0].city
#

def test_backend_initialization():
    rest_client = flexmock(client=flexmock())
    flexmock(ubersmith_client.api).should_receive('init').once()\
        .with_args(url='http://ubersmith.example', user='username', password='password')\
        .and_return(rest_client)

    UbObjectClient(url='http://ubersmith.example', user='username', password='password')
    # rest_client.client.should_receive('list').with_args().and_return([])
    # api = UbObjectClient(url='http://ubersmith.com/api/2.0/', user='username', password='password')
    # api.client.list()
