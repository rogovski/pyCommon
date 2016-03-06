import uuid
from   ..either import core as either

# base command object
class EVENT(object):
  def __init__(self, eventType, eventId=None, timeStamp=None, data=None):
    self.eventType = eventType
    self.eventId   = eventId
    self.timeStamp = timeStamp
    self.data      = data

  def get(self, key):
    if self.data is None:
      return either.Left('command has no data')

    if key not in self.data:
      return either.Left('command data key not found')

    return either.Right(self.data[key])
