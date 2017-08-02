class StrictConverter:
    def get(self, data, item, item_type):
        try:
            value = data[item]
        except KeyError:
            raise AttributeError

        if type(value) is not item_type:
            raise TypeError("Expected type={}, actual={}".format(item_type, type(value)))

        return data[item]


class BestEffortConverter:
    def get(self, data, item, item_type):
        try:
            return data[item]
        except KeyError:
            if not item_type:
                return None
            return item_type()
