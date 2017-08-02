from ub_object_client.client import Client
from ub_object_client.conversion import ApiConverter


class ClientApi(object):
    def __init__(self, api):
        self.api = api

    def list(self):
        client_list = self.api.client.list()

        return [Client(converter=ApiConverter(), **data) for data in client_list.values()]
