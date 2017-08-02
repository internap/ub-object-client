class Property:
    def __init__(self, type, reference_attribute):
        self.type = type
        self.reference_attribute = reference_attribute


class LegacyProperty:
    def __init__(self, use_instead):
        self.type = use_instead.type
        self.reference_attribute = use_instead.reference_attribute


class AutomagicMixin:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, attribute_name):
        value = object.__getattribute__(self, attribute_name)
        if attribute_name is not '_data':
            if isinstance(value, (Property, LegacyProperty)):
                try:
                    data = object.__getattribute__(self, '_data')
                except AttributeError:
                    return value
                return value.type(data[value.reference_attribute])
        return value
