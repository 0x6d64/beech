#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import json

import beech.entries
import beech.encoder_decoder

if __name__ == "__main__":
    ets = beech.entries.Entries()
    ets.new_diary_entry("Liebes Tagebuch, heute war ein schoener Tag.")
    ets.new_measurement_entry('bodyweight', 85.7, 'kg')
    ets.new_entry(beech.entries.Diary, text='test 123')
    ets.new_entry(beech.entries.Measurment, signal='foo', value=23.14)

    foo = json.dumps(ets, indent=2, skipkeys=True, cls=beech.encoder_decoder.MyEncoder)

    with open('dump.json', 'w') as fp:
        fp.write(foo)

    with open('dump.json', 'r') as fp:
        ets_loaded = json.load(fp, cls=beech.encoder_decoder.MyDecoder)

    with open('dump2.json', 'w') as fp:
        json.dump(ets_loaded, fp, cls=beech.encoder_decoder.MyEncoder, indent=2, skipkeys=True)

    for item_foo, item_bar in zip(ets, ets_loaded):
        print(item_foo)
        print(item_bar)
