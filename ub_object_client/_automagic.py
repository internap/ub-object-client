import warnings


class Property:
    def __init__(self, type, reference_attribute):
        self._type = type
        self.reference_attribute = reference_attribute

    def evaluate(self, value):
        return self._type(value)


class LegacyProperty:
    def __init__(self, use_instead):
        self._use_instead = use_instead
        self.reference_attribute = use_instead.reference_attribute

    def evaluate(self, value):
        warnings.warn("This property is supported for legacy usage only", DeprecationWarning)
        return self._use_instead.evaluate(value)


class LambdaProperty:
    def __init__(self, method, reference_attribute):
        self._method = method
        self.reference_attribute = reference_attribute

    def evaluate(self, value):
        return self._method(value)


class AutomagicMixin:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, attribute_name):
        value = object.__getattribute__(self, attribute_name)
        if attribute_name is not '_data':
            if isinstance(value, (Property, LegacyProperty, LambdaProperty)):
                try:
                    data = object.__getattribute__(self, '_data')
                except AttributeError:
                    return value
                return value.evaluate(data[value.reference_attribute])
        return value
