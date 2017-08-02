def apply_kwargs(kwargs, default_kwargs):
    for k, v in kwargs.items():
        if isinstance(v, dict):
            default_kwargs[k] = apply_kwargs(v, default_kwargs[k])
        else:
            default_kwargs[k] = v
    return default_kwargs


def a_client_list(*clients):
    return {c["clientid"]: c for c in sorted(clients, key=lambda e: e["clientid"])}


def a_client_from_client_list(**overrides):
    return apply_kwargs(overrides, {
        "clientid": "1",
        "first": "John",
        "last": "Doe",
        "checkname": "",
        "company": "Foobar Industries",
        "address": "New york i guess",
        "city": "New York",
        "state": "NY",
        "zip": "90210",
        "phone": "1234567890",
        "fax": "",
        "ss": "",
        "email": "email@example.org",
        "comments": "",
        "country": "US",
        "balance": "0.00",
        "credit_balance": "0.00",
        "acct_balance": "0.00",
        "datesend": "3",
        "datepay": "0",
        "password": "MEH",
        "active": "0",
        "permnote": None,
        "tempnote": None,
        "priority": "1",
        "class_id": "1",
        "login": "username1",
        "crv": "0",
        "chost": None,
        "clogin": None,
        "cpass": None,
        "access": "a:0:{}",
        "retry_every": "1",
        "referred": "",
        "referred_by": "0",
        "credit_bool": "0",
        "commission_rate": "0.00",
        "commission_type": "0",
        "commission": "0.00",
        "tier_commission_rate": "0.00",
        "tier_commission_type": "0",
        "tier_commission": "0.00",
        "sales": "0",
        "tier_sales": "0",
        "discount": "0.00",
        "latest_inv": "1412310654",
        "metadata": None,
        "datedue": "1",
        "grace_due": "0",
        "listed_company": "Foobar Industries",
        "full_name": "John Doe",
        "created": "1399127048",
        "password_timeout": "0",
        "password_changed": "1399598318",
        "charge_days": "0",
        "discount_type": "0",
        "qblistid": "",
        "qbeditseq": "",
        "prefer_lang": "0",
        "acctmgr": "0",
        "salesperson": "0",
        "late_fee_scheme_id": "0",
        "invoice_delivery": "1",
        "business": "1",
        "prebill_method": "1",
        "prebill_days": "0",
        "default_renew": "0",
        "prorate_min_days": "0",
        "auto_apply_credit": "1",
        "inv_balance": "0.00",
        "managed": "Unmanaged",
        "customer_record_type": ""
    })
