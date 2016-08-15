#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json

import beech.entries
from beech.exceptions import FileFormatError
from json.decoder import WHITESPACE

_ISO_FORMAT_STRING = '%Y-%m-%dT%H:%M:%S.%f'


class MyEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, datetime.datetime):
            return value.strftime(_ISO_FORMAT_STRING)
        else:
            return value.__dict__


class MyDecoder(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
        if isinstance(s, basestring):
            try:
                d = datetime.datetime.strptime(s, _ISO_FORMAT_STRING)
                return d
            except ValueError:
                decoded = super(MyDecoder, self).decode(s)
                if '_entries' in decoded:
                    ets = beech.entries.Entries()
                    for item in decoded['_entries']:
                        entry = self.decode(item)
                        ets.add_entry(entry)
                    return ets
                else:
                    raise FileFormatError('format error: did not find entries or date')
        else:
            json_type = s.get('entry_type', None)
            if json_type:
                if json_type == 'diary':
                    retval = beech.entries.Diary()
                    retval.text = s['_text']
                elif json_type == 'measurement':
                    retval = beech.entries.Measurment(s['signal'], s['value'], s['unit'])
                elif json_type == 'generic':
                    retval = beech.entries.Entry()
                else:
                    raise FileFormatError('could not determine entry_type, got {!s}'.format(json_type))
                retval.uuid = s['uuid']
                retval.date = self.decode(s['_Entry__date'])
                return retval
            else:  # no entry_type in JSON
                raise FileFormatError('expected entry_type, none found!')
