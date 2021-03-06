#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import uuid

dateParseFormat = '%Y-%m-%d'


class Entries(object):
    def __init__(self):
        self._entries = list()
        pass

    def new_entry(self, entry_type, **kwargs):
        entry = entry_type.get_new_obj(**kwargs)
        self.add_entry(entry)
        pass

    def new_measurement_entry(self, signal, value, unit=None):
        m = Measurment(signal, value, unit)
        self.add_entry(m)

    def new_diary_entry(self, text):
        d = Diary(text)
        self.add_entry(d)

    def add_entry(self, entry):
        self._entries.append(entry)

    def __iter__(self):
        return self._entries.__iter__()

    def __len__(self):
        return len(self._entries)

    def __str__(self):
        entrystrings = list()
        for item in self._entries:
            entrystrings.append(str(item))
        return '\n'.join(entrystrings)


class Entry(object):
    """
    class that defines a generic entry
    only metatdata attached are the entry_type, date and a uuid
    """

    def __init__(self, date=None):
        self.entry_type = 'generic'
        self.__date = datetime.datetime.now() if date is None else date
        self.uuid = uuid.uuid4().hex

    @classmethod
    def get_new_obj(cls, **kwargs):
        return Entry(**kwargs)

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if isinstance(value, datetime.datetime):
            self.__date = value
        else:
            self.__date = datetime.datetime.strptime(value, dateParseFormat)

    def __str__(self):
        return 'generic entry, date {}'.format(self.date)


class Diary(Entry):
    """
    adds a text property to the basic :class:`.Entry` class
    """

    def __init__(self, text=None):
        super(Diary, self).__init__()
        self.entry_type = 'diary'
        self._text = text

    @classmethod
    def get_new_obj(cls, **kwargs):
        return Diary(**kwargs)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if isinstance(text, basestring):
            self._text = text
        else:
            raise TypeError("text for a diary entry must be of entry_type basestring")

    def __str__(self):
        # return 'text: ' + str(self.text)
        return 'text: ' + self.text


class Measurment(Entry):
    """
    class that defines a measurement
    """

    def __init__(self, signal, value, unit=None):
        super(Measurment, self).__init__()
        self.entry_type = 'measurement'
        self.signal = signal
        self.value = value
        self.unit = 'no unit' if unit is None else unit

    @classmethod
    def get_new_obj(cls, **kwargs):
        return Measurment(**kwargs)

    def __str__(self):
        return 'signal: %s, value: %g %s' % (self.signal, self.value, self.unit)
