class Client:
    # _attrs = [
    #     ('clientid', int)
    #
    # ]

    @property
    def clientid(self):
        return int(self._data["clientid"])

    @property
    def first(self):
        return self._data["first"]

    def __init__(self, data):
        self._data = data
