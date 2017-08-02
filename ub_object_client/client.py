from ub_object_client._automagic import Property, LegacyProperty, AutomagicMixin


class StaticClient:
    def __init__(self, data):
        self._data = data

    @property
    def clientid(self):
        return int(self._data['clientid'])

    @property
    def first(self):
        return self._data["first"]


class AutomagicClient(AutomagicMixin):
    def __init__(self, data):
        self.id = Property(int, 'clientid')
        self.first_name = Property(str, 'first')

        self.first = LegacyProperty(use_instead=self.first_name)
        self.clientid = LegacyProperty(use_instead=self.id)

        super(AutomagicClient, self).__init__(data)


class Client(StaticClient):
    pass
