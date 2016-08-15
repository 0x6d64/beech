#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import beech.entries
import beech.encoder
import json

if __name__ == "__main__":
    ets = beech.entries.Entries()
    ets.adddiary("Liebes Tagebuch, heute war ein schöner Tag.")
    ets.addmeasurement('bodyweight', 85.7, 'kg')

    foo = json.dumps(ets, indent=2, skipkeys=True, cls=beech.encoder.MyEncoder)

    with open('dump.json', 'w') as fp:
        fp.write(foo)

    with open('dump.json', 'r') as fp:
        ets_loaded = json.load(fp, cls=beech.encoder.MyDecoder)

    with open('dump2.json', 'w') as fp:
        json.dump(ets_loaded, fp, cls=beech.encoder.MyEncoder, indent=2, skipkeys=True)

    for item_foo, item_bar in zip(ets, ets_loaded):
        print item_foo
        print item_bar
