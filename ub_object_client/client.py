class StaticClient:
    def __init__(self, data):
        self._data = data

    @property
    def clientid(self):
        return int(self._data['clientid'])

    @property
    def first(self):
        return self._data["first"]


class AutomagicClient:
    def __init__(self, data):
        self._data = data

    clientid = (int, 'clientid')
    first = (str, 'first')

    # id = alias(clientid)
    # test = (lambda test: int(test), 'test')

    def __getattribute__(self, attribute_name):
        _type = super(AutomagicClient, self).__getattribute__(attribute_name)[0]
        attribute_value = object.__getattribute__(self, '_data')[attribute_name]
        return _type(attribute_value)


class Client(StaticClient):
    pass
