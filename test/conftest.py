import pytest
import ubersmith_client
from flexmock import flexmock

from ub_object_client import UbObjectClient


@pytest.fixture
def api():
    rest_client = flexmock(
        client=flexmock()
    )
    flexmock(ubersmith_client.api).should_receive('init').and_return(rest_client)
    return UbObjectClient(url='', user='', password=''), rest_client
