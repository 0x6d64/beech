#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import os
import sys
import unittest

import beech.encoder_decoder
import beech.entries

testfile = 'test_dump.json'


class TestJsonDumpAndLoad(unittest.TestCase):
    def test_dump(self):
        """
        do the dumping and check for Exceptions
        """
        self.clear_file_if_present(testfile)

        # noinspection PyBroadException
        try:
            with open(testfile, 'w') as fp:
                json.dump(self._get_entries(), fp, cls=beech.encoder_decoder.MyEncoder)
            self.clear_file_if_present(testfile)
        except Exception:
            e = sys.exc_info()[0]
            self.fail('exception should not be raised, got {!s}'.format(e))
        pass

    def test_load(self):
        """
        write example dump and check:
        - that load data is of type Entries
        - that all items in _entries are of type Entry
        """
        self.clear_file_if_present(testfile)

        with open(testfile, 'w') as fp:
            json.dump(self._get_entries(), fp, cls=beech.encoder_decoder.MyEncoder)

        with open(testfile, 'r') as fp:
            data = json.load(fp, cls=beech.encoder_decoder.MyDecoder)

        self.assertIsInstance(data, beech.entries.Entries,
                              'Loaded data is not of entry_type Entries, got {!s} instead!'.format(type(data)))
        for item in data:
            self.assertIsInstance(item, beech.entries.Entry)

    def test_dump_and_load(self):
        self.clear_file_if_present(testfile)

        original = self._get_entries()

        with open(testfile, 'w') as fp:
            json.dump(original, fp=fp, indent=2, skipkeys=True, cls=beech.encoder_decoder.MyEncoder)
        with open(testfile, 'r') as fp:
            loaded = json.load(fp, cls=beech.encoder_decoder.MyDecoder)

        for a, b in zip(original, loaded):
            print('{!s}\n{!s}'.format(a, b))
            self.assertEqual(str(b), str(a))

    @staticmethod
    def _get_entries(umlauts=False):
        ets = beech.entries.Entries()
        ets.new_diary_entry("Liebes Tagebuch, heute war ein sch{}ner Tag.".format('ö' if umlauts else 'oe'))
        ets.new_measurement_entry('bodyweight', 85.7, 'kg')
        entry = beech.entries.Entry()
        entry.uuid = '0815'
        ets.add_entry(entry)
        return ets

    @staticmethod
    def clear_file_if_present(filename):
        if os.path.exists(filename):
            os.remove(filename)
