from ..data import command as base

# get the information of currently loaded datasource
class GET_DATASOURCE_INFO_REQUESTED(base.COMMAND):
    def __init__(self, data):
        super(GET_DATASOURCE_INFO_REQUESTED, self) \
            .__init__('GET_DATASOURCE_INFO_REQUESTED', data=data)

# load datasource
class LOAD_DATASOURCE_REQUESTED(base.COMMAND):
    def __init__(self, data):
        super(LOAD_DATASOURCE_REQUESTED, self) \
            .__init__('LOAD_DATASOURCE_REQUESTED', data=data)
