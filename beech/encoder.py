#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import datetime

_ISO_FORMAT_STRING = '%Y-%M-%DT%H:%M:%S.%mmmmm'


class MyEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, datetime.datetime):
            return value.strftime(_ISO_FORMAT_STRING)
        else:
            return value.__dict__


class MyDecoder(json.JSONDecoder):
    def decode(self, s):
        try:
            d = datetime.datetime.strptime(s, _ISO_FORMAT_STRING)
            return d
        except ValueError:
            return super(MyDecoder, self).decode(s)
