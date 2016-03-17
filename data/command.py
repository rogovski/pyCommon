import uuid
import time
from   ..either import core as either

# base command object
class COMMAND(object):
    def __init__(self,
                 commandType,
                 data=None):

        self.commandType = commandType
        self.commandId   = str(uuid.uuid4())
        self.timeStamp   = time.time()
        self.data        = data

    def getData(self,
                key):

        if self.data is None:
            return either.Left('command has no data')

        if key not in self.data:
            return either.Left('command data key not found')

        return either.Right(self.data[key])