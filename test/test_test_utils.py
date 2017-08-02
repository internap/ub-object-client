import pytest

from ub_object_client.client import Client
from ub_object_client.test_utils import StrictConverter, BestEffortConverter


def test_strict_conversion_with_partial_client():
    client = Client(converter=StrictConverter(), clientid=1)
    assert client.clientid == 1
    with pytest.raises(AttributeError):
        client.address

    with pytest.raises(AttributeError):
        client.undefined_property


def test_best_effort_conversion_with_partial_client():
    client = Client(converter=BestEffortConverter(), clientid=1)
    assert client.clientid == 1
    assert client.address == ''
    assert client.undefined_property is None


def test_client_stub_same_as_best_effort():
    client = Client()
    assert client.address == ''
    assert client.undefined_property is None
