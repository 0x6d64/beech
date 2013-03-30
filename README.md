#Beech
A simple diary/lifelog system implemented in python. For Version info see the [history file](HISTORY.md).

##Purpose
Time is limited, so I will make this short: I wanted to have a simpler method to write my diary. And even more badly I wanted to have a diary that gives back entries of a certain time range (e.g. all of the last week). Sounds like a sweet project to play around with python for the first time, right? My plan is to keep it simple and add features as I need them.

##Features
###Planned for version 0.1
- simple method of entry

###Planned for version 0.2
- implementation of a cache using the Python "pickle" mechanism. It will read the content of the markdown file into memory, perform the desired operations and then write it back not only into the markdown file, but also into a pickled cache. Subsequent operations can use the cache file (and thus omit parsing the markdown file), as long as the cache file is up-to-date (based on "last changed date" of the files). Writing into the markdown file outside of beech will trigger an update of the cache when beech is run the next time.
- beech reporting back entries for a certain time range, e.g. yesterday, last week, 30 days before

###Planned for future versions
- append a file to an entry, beech moves the file to a subdirectory, renames the file to a UNIX time stamp
- editing existing entries
- adding a location for an entry via the OS X core location framework
- parsing of an input file containing new entries. This will enable the user to use a service like [ittf.com](http://ittf.com) to send an email to an address, which then appends to a file in a dropbox folder (basic form of email-to-beech).
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
- Beech entry report is expected to be slow when the diary file grows to a larger size and no pickled cache is present
- ~~manual edits on the diary file will have to be made with some caution, since they have to be ordered by time (or return of diary entries will not work as expected)~~ I expect this to be solved by using a pickled cache.
- Beech was written by a python n00b with zero experience, don't expect elegant code.

#Developed by
Martin Demling, 0x6d64@martin-demling.de  

#License
[GPL V3.0](http://www.gnu.org/licenses/gpl-3.0.html)

