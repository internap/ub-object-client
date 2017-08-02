class StaticClient:
    def __init__(self, data):
        self._data = data
        self.clientid = int(self._data['clientid'])
        self.first = self._data['first']

class Client(StaticClient):
    pass
