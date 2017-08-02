import pytest

from ub_object_client.conversion import ConvertibleObject, ApiConverter, IntOrNone


class ConvertibleObjectStub(ConvertibleObject):
    def __init__(self, converter, **data):
        super(ConvertibleObjectStub, self).__init__(converter=converter, **data)
        self.str_type_attribute = str
        self.int_type_attribute = int
        self.defaulted = IntOrNone


def test_api_converter_with_basic_types():
    object = ConvertibleObjectStub(converter=ApiConverter(), **dict(
        str_type_attribute='test',
        int_type_attribute='3'
    ))

    assert object.str_type_attribute == 'test'
    assert object.int_type_attribute == 3


def test_api_converter_with_data_not_present_in_api():
    object = ConvertibleObjectStub(converter=ApiConverter())
    assert object.defaulted is None


def test_api_converter_lazy_evaluates_property():
    object = ConvertibleObjectStub(converter=ApiConverter(), **dict(
        int_type_attribute='test'
    ))
    with pytest.raises(ValueError):
        assert object.int_type_attribute
