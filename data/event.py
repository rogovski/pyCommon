import uuid

# base command object
class EVENT(object):
  def __init__(self):
    self.eventType = None
    self.eventId   = None
    self.timeStamp = None
