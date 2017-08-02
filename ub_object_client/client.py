from datetime import datetime

from ub_object_client.conversion import ConvertibleObject, Money, IntOrNone
from ub_object_client.test_utils import BestEffortConverter


class Client(ConvertibleObject):
    def __init__(self, converter=None, **data):
        super(Client, self).__init__(converter=converter or BestEffortConverter(), **data)

        self.clientid = int
        self.first = str
        self.balance = Money
        self.created = datetime
        self.prebill_days = int
        self.acct_balance = Money
        self.acctmgr = int
        self.active = int
        self.address = str
        self.auto_apply_credit = bool
        self.business = int
        self.charge_days = int
        self.checkname = str
        self.city = str
        self.class_id = int
        self.comments = str
        self.commission = Money
        self.commission_rate = Money
        self.commission_type = int
        self.company = str
        self.country = str
        self.credit_balance = Money
        self.credit_bool = bool
        self.crv = int
        self.datedue = bool
        self.discount = Money
        self.discount_type = int
        self.email = str
        self.fax = str
        self.full_name = str
        self.grace_due = int
        self.inv_balance = Money
        self.invoice_delivery = bool
        self.last = str
        self.late_fee_scheme_id = int
        self.latest_inv = datetime
        self.listed_company = str
        self.login = str
        self.managed = str
        self.password_timeout = int
        self.password_changed = datetime
        self.phone = datetime
        self.prebill_method = int
        self.prefer_lang = int
        self.priority = int
        self.prorate_min_days = int
        self.qblistid = IntOrNone
        self.retry_every = int
        self.state = str
        self.tier_commission = Money
        self.tier_commission_rate = Money
        self.tier_commission_type = int
        self.zip = str
