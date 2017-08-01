from flexmock import flexmock
import ubersmith_client
from ub_object_client import UbObjectClient


def test_client_list(api):
    api, rest_client = api
    rest_client.should_receive('list').and_return({
        "1001": {
            "city": "Troy",
        }
    })

    returned_object = api.client.list()

    assert "Troy" == returned_object[0].city
