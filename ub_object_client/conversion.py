from datetime import datetime


class Money:
    pass


class IntOrNone:
    pass


class ApiConverter:
    def get(self, data, item, item_type):
        value_str = data.get(item, "")
        if item_type == datetime:
            return datetime.utcfromtimestamp(float(value_str))
        if item_type in (str, bool, int):
            return item_type(value_str)
        if item_type is Money:
            return float(value_str)
        if item_type is IntOrNone:
            return int(value_str) if value_str else None


class ConvertibleObject:
    def __init__(self, converter, **data):
        self._converter = converter
        self._data = data

    def __getattribute__(self, item):
        def passthrough(field):
            return object.__getattribute__(self, field)

        if item.startswith('_'):
            return passthrough(item)

        _converter = passthrough('_converter')
        _data = passthrough('_data')
        try:
            item_type = passthrough(item)
        except AttributeError:
            item_type = None

        return _converter.get(_data, item, item_type)
