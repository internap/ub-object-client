from datetime import datetime


def to_money(str):
    return float(str)


def to_datetime(timestamp_str):
    return datetime.utcfromtimestamp(float(timestamp_str))


def int_or_none(str):
    if not str:
        return None
    return int(str)


class Client:
    def __init__(self, data):
        self._data = data

        self.clientid = int(data['clientid'])
        self.first = str(data['first'])
        self.balance = to_money(data['balance'])
        self.created = to_datetime(data['created'])
        self.prebill_days = int(data['prebill_days'])
        self.acct_balance = to_money(data['acct_balance'])
        self.acctmgr = int(data['acctmgr'])
        self.active = int(data['active'])
        self.address = str(data['address'])
        self.auto_apply_credit = bool(data['auto_apply_credit'])
        self.business = int(data['business'])
        self.charge_days = int(data['charge_days'])
        self.checkname = str(data['checkname'])
        self.city = str(data['city'])
        self.class_id = int(data['class_id'])
        self.comments = str(data['comments'])
        self.commission = to_money(data['commission'])
        self.commission_rate = to_money(data['commission_rate'])
        self.commission_type = int(data['commission_type'])
        self.company = str(data['company'])
        self.country = str(data['country'])
        self.credit_balance = to_money(data['credit_balance'])
        self.credit_bool = bool(data['credit_bool'])
        self.crv = int(data['crv'])
        self.datedue = bool(data['datedue'])
        self.discount = to_money(data['discount'])
        self.discount_type = int(data['discount_type'])
        self.email = str(data['email'])
        self.fax = str(data['fax'])
        self.full_name = str(data['full_name'])
        self.grace_due = int(data['grace_due'])
        self.inv_balance = to_money(data['inv_balance'])
        self.invoice_delivery = bool(data['invoice_delivery'])
        self.last = str(data['last'])
        self.late_fee_scheme_id = int(data['late_fee_scheme_id'])
        self.latest_inv = to_datetime(data['latest_inv'])
        self.listed_company = str(data['listed_company'])
        self.login = str(data['login'])
        self.managed = str(data['managed'])
        self.password_timeout = int(data['password_timeout'])
        self.password_changed = to_datetime(data['password_changed'])
        self.phone = to_datetime(data['phone'])
        self.prebill_method = int(data['prebill_method'])
        self.prefer_lang = int(data['prefer_lang'])
        self.priority = int(data['priority'])
        self.prorate_min_days = int(data['prorate_min_days'])
        self.qblistid = int_or_none(data['qblistid'])
        self.retry_every = int(data['retry_every'])
        self.state = str(data['state'])
        self.tier_commission = to_money(data['tier_commission'])
        self.tier_commission_rate = to_money(data['tier_commission_rate'])
        self.tier_commission_type = int(data['tier_commission_type'])
        self.zip = str(data['zip'])
