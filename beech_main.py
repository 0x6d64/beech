#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import beech.entries
import json

if __name__ == "__main__":
    ets = beech.entries.Entries()
    ets.adddiary("Liebes Tagebuch, heute war ein schöner Tag.")
    ets.addmeasurement('bodyweight', 85.7, 'kg')


    class MyEncoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__


    print(str(ets))
    for entry in ets:
        print(str(entry.__dict__))
        foo = json.dumps(entry, skipkeys=True, cls=MyEncoder)
    pass
