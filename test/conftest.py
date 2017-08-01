import pytest
import ubersmith_client
from flexmock import flexmock

from ub_object_client import UbObjectClient


@pytest.fixture
def api(ub):
    flexmock(ubersmith_client.api).should_receive('init').and_return(ub)
    return UbObjectClient(url='', user='', password='')


@pytest.fixture
def ub():
    return flexmock(
        client=flexmock()
    )
