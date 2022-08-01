import json
from decimal import *
from datetime import date


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        if isinstance(obj, date):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
