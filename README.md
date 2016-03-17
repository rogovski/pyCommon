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

A typical worker process is initialized as follows.

A process manager initializes a worker with two pieces of information.

1. <uuid-work-queue> - a uuid uniquely identifing the worker and the queue
that it consumes messages from.

2. <response-channel> - a channel that the worker broadcasts responses to
via redis publish

about this worker is stored in a redis hash

worker:<uuid-work-queue> = {
    startedOn:datetime,
    pid:int,
    responseChannel:<response-channel>
}

the worker initiates a client connection to the message broker (rabbitmq, SQS,
azureque). it connects to message broker with queue name <uuid-work-queue>.







1> GET_INFO_WORKER
2> GET_INFO_WORKER_FRAME_MANAGER
3> LOAD_WORKER_FRAME_MANAGER
4> KILL_WORKER_FRAME_MANAGER
5> MODIFY_WORKER_FRAME_MANAGER
6> SAVE_WORKER_FRAME_MANAGER
7> LOAD_STREAM_WORKER_FRAME_MANAGER
8> KILL_STREAM_WORKER_FRAME_MANAGER





1a< GET_INFO_WORKER_SUCCEEDED
1b< GET_INFO_WORKER_FAILED