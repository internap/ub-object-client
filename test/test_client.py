import datetime

import pytest
from test import fixtures


def test_client_list_no_client(api, ub):
    ub.client.should_receive('list').and_return(fixtures.a_client_list())

    assert api.client.list() == []


def test_client_fields_are_converted_properly(ub, api):
    ub.client.should_receive('list').and_return(
        fixtures.a_client_list(
            fixtures.a_client_from_client_list(
                clientid='1',
                first='John',
                balance="0.00",
                created="1399127048"
            )
        )
    )
    client = api.client.list()[0]

    assert client.clientid == 1
    assert type(client.clientid) == int

    assert client.first == "John"
    assert type(client.first) == str
    assert client.balance == 0.0
    assert type(client.balance) == float

    assert client.created == datetime.datetime(2014, 5, 3, 14, 24, 8)
    assert type(client.created) == datetime.datetime


def test_all_client_list_fields_are_present(ub, api):
    client = fixtures.a_client_from_client_list()

    ub.client.should_receive('list').and_return(fixtures.a_client_list(client))
    objectified_client = api.client.list()[0]

    unsupported_fields = [
        'access',
        'chost',
        'clogin',
        'cpass',
        'customer_record_type',
        'datepay',
        'datesend',
        'default_renew',
        'metadata',
        'password',
        'permnote',
        'tempnote',
        'qbeditseq',
        'referred',
        'referred_by',
        'sales',
        'salesperson',
        'ss',
        'tier_sales'
    ]
    fields = client.keys()
    for field in sorted(fields - unsupported_fields):
        try:
            getattr(objectified_client, field)
        except AttributeError:
            pytest.fail("Field {} was not found".format(field))
