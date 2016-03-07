from ..data import event as base

# get the information of currently loaded datasource
class GET_DATASOURCE_INFO_SUCCEEDED(base.EVENT):
    def __init__(self, data):
        super(GET_DATASOURCE_INFO_SUCCEEDED, self) \
          .__init__('GET_DATASOURCE_INFO_SUCCEEDED', data=data)

# get the information of currently loaded datasource
class GET_DATASOURCE_INFO_FAILED(base.EVENT):
    def __init__(self, data):
        super(GET_DATASOURCE_INFO_FAILED, self) \
          .__init__('GET_DATASOURCE_INFO_FAILED', data=data)

# load datasource
class LOAD_DATASOURCE_SUCCEEDED(base.EVENT):
    def __init__(self, data):
        super(LOAD_DATASOURCE_SUCCEEDED, self) \
          .__init__('LOAD_DATASOURCE_SUCCEEDED', data=data)

# load datasource
class LOAD_DATASOURCE_FAILED(base.EVENT):
    def __init__(self, data):
        super(LOAD_DATASOURCE_FAILED, self) \
          .__init__('LOAD_DATASOURCE_FAILED', data=data)

# load datasource
class UNKNOWN_EVENT_RECEIVED(base.EVENT):
    def __init__(self, data):
        super(UNKNOWN_EVENT_RECEIVED, self) \
          .__init__('UNKNOWN_EVENT_RECEIVED', data=data)
