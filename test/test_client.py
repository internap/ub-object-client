from flexmock import flexmock
import ubersmith_client
from ub_object_client import UbObjectClient


def test_client_list(api, ub):
    # api, ub = api
    ub.client.should_receive('list').and_return({
        "1001": {
            "city": "Troy",
        }
    })

    returned_object = api.client.list()

    assert "Troy" == returned_object[0].city


def test_client_list_no_client(api, ub):
    ub.client.should_receive('list').and_return({})

    assert api.client.list() == []


def test_client_with_some_fields(ub, api):
    ub.client.should_receive('list').and_return({
        "1": {
            "clientid": "1",
            "first": "Philippe",
            "last": "Godin",
            "checkname": "",
            "company": "iWeb Technologies",
            "address": "20 Place du Commerce",
            "city": "Montréal",
            "state": "QC",
            "zip": "H3E 1Z6",
            "phone": "5142864242",
            "fax": "",
            "ss": "",
            "email": "pgodin@iweb.com",
            "comments": "",
            "country": "CA",
            "balance": "0.00",
            "credit_balance": "0.00",
            "acct_balance": "0.00",
            "datesend": "3",
            "datepay": "0",
            "password": "{ssha1}6mvKokNgYeTjASFpKmU9MQya0/ZnZFc2",
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
            "access": "a:66:{s:14:\"client_profile\";s:4:\"edit\";s:12:\"view_profile\";s:4:\"edit\";s:17:\"view_billing_info\";s:4:\"edit\";s:15:\"change_password\";s:4:\"view\";s:15:\"manage_contacts\";s:4:\"edit\";s:25:\"manage_contact_facilities\";s:4:\"edit\";s:16:\"billing_services\";s:4:\"edit\";s:12:\"view_invoice\";s:4:\"edit\";s:12:\"view_service\";s:4:\"edit\";s:19:\"view_tax_exemptions\";s:4:\"edit\";s:12:\"view_credits\";s:4:\"edit\";s:11:\"view_orders\";s:4:\"edit\";s:20:\"paypal_subscriptions\";s:4:\"edit\";s:11:\"view_quotes\";s:4:\"edit\";s:13:\"billing_email\";s:4:\"edit\";s:7:\"reports\";s:4:\"edit\";s:9:\"event_log\";s:4:\"edit\";s:16:\"ledger_event_log\";s:4:\"edit\";s:8:\"mail_log\";s:4:\"edit\";s:17:\"domain_management\";s:4:\"edit\";s:12:\"list_domains\";s:4:\"edit\";s:13:\"lookup_domain\";s:4:\"edit\";s:7:\"support\";s:4:\"edit\";s:12:\"view_tickets\";s:4:\"edit\";s:17:\"submit_new_ticket\";s:4:\"edit\";s:16:\"view_all_tickets\";s:4:\"view\";s:13:\"search_ticket\";s:4:\"view\";s:14:\"device_manager\";s:4:\"edit\";s:11:\"view_device\";s:4:\"edit\";s:10:\"view_racks\";s:4:\"edit\";s:10:\"view_cages\";s:4:\"edit\";s:15:\"view_facilities\";s:4:\"edit\";s:17:\"view_ip_addresses\";s:4:\"edit\";s:13:\"custom_link_2\";s:4:\"view\";s:13:\"custom_link_5\";s:4:\"view\";s:13:\"custom_link_4\";s:4:\"view\";s:13:\"custom_link_8\";s:4:\"view\";s:13:\"custom_link_9\";s:4:\"view\";s:14:\"custom_link_10\";s:4:\"view\";s:14:\"custom_link_11\";s:4:\"view\";s:14:\"custom_link_12\";s:4:\"view\";s:14:\"custom_link_13\";s:4:\"view\";s:14:\"custom_link_15\";s:4:\"view\";s:14:\"custom_link_14\";s:4:\"view\";s:9:\"hapi_test\";s:2:\"15\";s:9:\"hapi_uber\";s:2:\"15\";s:9:\"hapi_hapi\";s:2:\"15\";s:19:\"hapi_hapi_auth_read\";s:2:\"15\";s:21:\"hapi_hapi_auth_manage\";s:2:\"15\";s:12:\"hapi_devices\";s:2:\"15\";s:12:\"hapi_backups\";s:2:\"15\";s:12:\"hapi_metrics\";s:2:\"15\";s:13:\"hapi_monitors\";s:2:\"15\";s:10:\"hapi_power\";s:2:\"15\";s:15:\"hapi_facilities\";s:2:\"15\";s:8:\"hapi_ips\";s:2:\"15\";s:13:\"hapi_voxcloud\";s:2:\"15\";s:16:\"hapi_config_mgmt\";s:2:\"15\";s:20:\"hapi_platformconnect\";s:2:\"15\";s:12:\"hapi_billing\";s:2:\"15\";s:13:\"hapi_voxfiles\";s:2:\"15\";s:12:\"hapi_support\";s:2:\"15\";s:9:\"hapi_jobs\";s:2:\"15\";s:8:\"hapi_cdn\";s:2:\"15\";s:8:\"hapi_dns\";s:2:\"15\";s:10:\"hapi_agile\";s:2:\"31\";}",
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
            "listed_company": "iWeb Technologies",
            "full_name": "Philippe Godin",
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
        }})
    client = api.client.list()[0]

    assert client.clientid == 1
