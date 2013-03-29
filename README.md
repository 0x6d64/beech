#Beech
A simple diary/lifelog system implemented in python. For Version info see the [history file](HISTORY.md).

##Purpose
Time is limited, so I will make this short: I wanted to have a simpler method to write my diary. And even more badly I wanted to have a diary that gives back entries of a certain time range (e.g. all of the last week). Sounds like a sweet project to play around with python for the first time, right? My plan is to keep it simple and add features as I need them.

##Features
###Planned for version 0.1
- simple method of entry

###Planned for version 0.2
- beech reporting back entries for a certain time range, e.g. yesterday, last week, 30 days before

###Planned for future versions
- append a file to an entry, beech moves the file to a subdirectory, renames the file to a UNIX time stamp
- editing existing entries
- adding a location for an entry via the OS X core location framework
- *your suggestion*

##Usage
*to be added*

##Data format
The beech data format is made to be human readable, so the entries are written using markdown. Dates are noted using a h1 heading, times in a h2 heading. Example markdown source:

    #date: 01.03.2013
    ##time: 23.42
    Text of the first example entry.
    ##time: 23.59
    Second example entry.
    New lines will facilitate grepping the diary file.
    
This will render like this:

>#date: 01.03.2013
>##time: 23.42
>Text of the first example entry.
>##time: 23.59
>Second example entry.
>New lines will facilitate grepping the diary file.

##Known issues
- Beech entry report is expected to be slow when the diary file grows to a larger size
- Beech was written by a python n00b with zero experience, don't expect elegant code.

#Developed by
Martin Demling, 0x6d64@martin-demling.de  

#License
[GPL V3.0](http://www.gnu.org/licenses/gpl-3.0.html)

