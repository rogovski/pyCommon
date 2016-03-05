import uuid

# base command object
class COMMAND(object):
  def __init__(self):
    self.commandType = None
    self.commandId   = None
    self.timeStamp   = None
