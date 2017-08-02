import ubersmith_client
from ub_object_client.ubersmith_object_api import ClientApi


class UbObjectClient:
    def __init__(self, url, user, password):
        self.api = ubersmith_client.api.init(url=url, user=user, password=password)

    @property
    def client(self):
        return ClientApi(self.api)
