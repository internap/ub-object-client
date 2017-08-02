from datetime import datetime

from ub_object_client._automagic import Property, LegacyProperty, AutomagicMixin, LambdaProperty

DATETIME_LAMBDA = lambda timestamp_str: datetime.fromtimestamp(float(timestamp_str))


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
        self.created = LambdaProperty(DATETIME_LAMBDA, 'created')

        self.clientid = LegacyProperty(use_instead=self.id)
        self.first = LegacyProperty(use_instead=self.first_name)

        super(AutomagicClient, self).__init__(data)


class Client(StaticClient):
    pass
