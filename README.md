# Beech

**Note**: This project is no longer under development. I never used it productively, but it turned out 
to be a good exercise to implement the things present in this repo.

A simple diary/lifelog system implemented in python. For Version info see the [history file](HISTORY.md).

## Purpose
- Have a unified place/format to store data on myself (think diary + runkeeper + beeminder + facebook updates). Own the data and have it in an open format without any lock in or third party snooping around.
- Later maybe learn interesting stuff or surprising patterns in my own life.
- have a project to develop my OOP skills
- have meaningful data to dive into couchdb

## Use cases

### High priority
- write a few paragraphs of text as a diary entry
- record my body weight on a regular basis
- create a script that pulls statistics like the number of pending tasks in taskwarrior and stores it in the database
- retrieve entries from a certain period of time (e.g. from a year ago) and present it
- create reports or graphs of numeric measurements and display them

### Medium priority
- have a nice looking interface

### Low priority
- have data on several devices synchronize

## Requirements
- use a human readable data format
- can easily be expanded to store additional types of data
- is robust to accommodate later additions like sorting, merging, splitting up data, syncing

## Implementation
### Storage
JSON, as it seems to be a good choice for a collection of events that have a varying number of attributes. The idea is to have an JSON object for every entry, and have those required attributes:

- a unique ID
- a type

The first types I plan to implement are the "diary"" and the "measurement" type which both need a timestamp (ISO8601) and "data".

## Roadmap
### Planned for version 0.1
- basic entry class
- diary and measurement classes
- unit test all the things

### Planned for version 0.2
- write and read state to disk
- merge data files

### Planned for future versions
- not decided yet 

--------
*Developed by*:

Martin Demling, 0x6d64@martin-demling.de  

*License:*

[GPL V3.0](http://www.gnu.org/licenses/gpl-3.0.html)

