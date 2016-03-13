import uuid
from   ..either import core as either

# base command object
class COMMAND(object):
    def __init__(self, 
                 commandType, 
                 commandId=None, 
                 timeStamp=None, 
                 data=None):

        self.commandType = commandType
        self.commandId   = commandId
        self.timeStamp   = timeStamp
        self.data        = data

    def get(self, 
            key):
    
        if self.data is None:
            return either.Left('command has no data')

        if key not in self.data:
            return either.Left('command data key not found')

        return either.Right(self.data[key])