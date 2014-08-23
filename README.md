#Beech
A simple diary/lifelog system implemented in python. For Version info see the [history file](HISTORY.md).

##Purpose
Have a unified place/format to store data on myself (think diary + runkeeper + beeminder + facebook updates). Own the data and have it in an open format without any lock in or third party snooping around.
Later maybe learn interesting stuff or surprising patterns in my own life.

##Requirements
- use a human readable data format
- can easily be expanded to store additional types of data
- is robust to accomodate later additions like sorting, merging, splitting up data, syncing

##Implementation
###Storage
JSON, as it seems to be a good choice for a collection of events that have a varying number of attributes. The idea is to have an JSON object for every entry, and have those required attributes:

- a unique ID
- a type

The first types I plan to implement are the "diary"" and the "measurement" type which both need a timestamp (ISO8601) and "data".


###Data manipulation
The next thing to implement will be some python methods for entering and retrieving data. Wrappers for those will follow.


##Roadmap
###Planned for version 0.1
- simple method of entry

###Planned for version 0.2
- not decided yet 

###Planned for future versions
- not decided yet 

--------
*Developed by*:

Martin Demling, 0x6d64@martin-demling.de  

*License:*

[GPL V3.0](http://www.gnu.org/licenses/gpl-3.0.html)

