import ubersmith_client


class UbObjectClient:
    def __init__(self, url, user, password):
        self.api = ubersmith_client.api.init(url=url, user=user, password=password)

