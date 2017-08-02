from ub_object_client.client import Client


class ClientApi(object):
    def __init__(self, api):
        self.api = api

    def list(self):
        client_list = self.api.client.list()

        return [Client(data) for data in client_list.values()]


def _patch_matching_attributes(client, attributes):
    for k, v in attributes.items():
        if hasattr(client, k):
            setattr(client, k, v)
    return client
