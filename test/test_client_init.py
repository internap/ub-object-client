from flexmock import flexmock
import ubersmith_client
from ub_object_client import UbObjectClient


def test_backend_initialization():
    rest_client = flexmock(client=flexmock())
    flexmock(ubersmith_client.api).should_receive('init').once()\
        .with_args(url='http://ubersmith.example', user='username', password='password')\
        .and_return(rest_client)

    UbObjectClient(url='http://ubersmith.example', user='username', password='password')
