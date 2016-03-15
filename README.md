# pyCommon

common python functionality

## pyCommon.data

general data utilities

### pyCommon.data.command

base COMMAND object. represents a command sent to a system. all interaction
with a system initiates with a COMMAND object.

### pyCommon.data.event

base EVENT object. represents a transaction that has taken place in a system.
EVENTs are generated in response to COMMANDs. EVENTs are always named after
past tense verbs

### pyCommon.data.frame

container that imbues a pandas data frame with extra functionality

### pyCommon.data.query

utilities for querying datasources. includes pandas dataframes, sql stores,
and redis.

### pyCommon.data.serialize

utilities for serializing data into/out of system.

## pyCommon.either

either monad

### pyCommon.either.core

core functionality of either monad. Implements Left, Pending, and Right.
implements a pipe operation similar to haskell's '>=>' (reverse compose).

## pyCommon.net

network functionality


### pyCommon.net.process

A networked interface over pandas data frames. supports the ability
to manipulate/query data over a network protocol (tcp?)

GET /
- fetch dataset loaded by process. returns empty if no dataset is loaded
- this opens up issues concerning data size. maybe we add in some paging
  mechanism

POST /
- load dataset into process local storage. if the dataset does not exist,
  notify requester and do nothing.

GET /info
- get general info of process and dataset.

GET /features
- return feature information of the dataset.

POST /features
- set (or override) feature info of dataset. if no dataset is loaded notify
  requester and do nothing

POST /kill
- kill the process

POST /push
- start pushing the dataset to a specified destination. if the process is
  already pushing, do nothing. if destination does not exist, notify and
  do nothing

POST /stop
- stop pushing the dataset. if the process is already stopped, do nothing.



### COMMANDS

1> GET_WORKER_INFO
2> LOAD_WORKER_FRAME_MANAGER
3> GET_WORKER_FRAME_MANAGER_INFO
4> STREAM_WORKER_FRAME_MANAGER





1a< GET_WORKER_INFO_SUCCEEDED
1b< GET_WORKER_INFO_FAILED