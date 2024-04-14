#!/usr/bin/env python3


import datetime


global project
project = "Testing"

global tester
tester = "Ursa"

global docs
docs = {"NDA": False, "SOW": False, "ROE": False, "Approval": False, "3rd Party": False, "Other": False}

global engagement_type
engagement_type = {"Black Box": False, "White Box": False, "Grey Box": False}

global engagement_scope
engagement_scope = {"Physical": False, "Remote": False, "Full-spec": False, "Wireless": False, "Web": False, "App": False, "SocEng": False, "Rogue": False, "Inside": False, "DoS": False}

global timeline
timeline = {"from": datetime.date.today(), "to": (datetime.date.today() + datetime.timedelta(days=7)), "Status Updates": {"Daily": False, "Weekly": False, "Monthly": False, "Quarterly": False}}

