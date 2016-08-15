#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import os
import sys
import time
import unittest

import beech.encoder
import beech.entries


class TestJsonDumpAndLoad(unittest.TestCase):
    def test_dump(self):
        testfile = 'jsontestfile.json'
        if os.path.exists(testfile):
            os.remove(testfile)
        time.sleep(0.3)

        try:
            with open(testfile, 'w') as fp:
                json.dump(self._get_entries(), fp, cls=beech.encoder.MyEncoder)
            os.remove(testfile)
        except:
            e = sys.exc_info()[0]
            self.fail('exception should not be raised, got {!s}'.format(e))
        pass

    def test_dump_and_load(self):
        ets = beech.entries.Entries()
        ets.adddiary("Liebes Tagebuch, heute war ein schöner Tag.")
        ets.addmeasurement('bodyweight', 85.7, 'kg')

        foo = json.dumps(ets, indent=2, skipkeys=True, cls=beech.encoder.MyEncoder)

        with open('dump.json', 'w') as fp:
            fp.write(foo)

        with open('dump.json', 'r') as fp:
            ets_loaded = json.load(fp, cls=beech.encoder.MyDecoder)

        for item_foo, item_bar in zip(ets, ets_loaded):
            print item_foo
            print item_bar
            self.assertEqual(str(item_bar), str(item_foo))

    def _get_entries(self):
        ets = beech.entries.Entries()
        ets.adddiary("Liebes Tagebuch, heute war ein schöner Tag.")
        ets.addmeasurement('bodyweight', 85.7, 'kg')
        return ets
