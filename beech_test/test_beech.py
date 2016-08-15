#!/usr/bin/env python

import unittest

import beech.entries


class TestEntries(unittest.TestCase):
    def setUp(self):
        self.entries = beech.entries.Entries()
        pass

    def tearDown(self):
        pass

    def test_entries_len(self):
        for count in xrange(0, 100):
            self.entries.new_diary_entry('Eintrag Nr. {!s}'.format(count))
            self.assertEqual(len(self.entries), count + 1)

    def test_adding_methods(self):
        self.entries.new_diary_entry('foo')
        self.entries.new_measurement_entry('signal', 23, 'unit')
        self.entries.new_entry(beech.entries.Entry)
        self.entries.new_entry(beech.entries.Diary)
        self.entries.new_entry(beech.entries.Measurment, signal='foo', value=10)

        self.assertEqual(len(self.entries), 5)


if __name__ == "main":
    pass
