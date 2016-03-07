from    ..either import core as either
import  pandas   as pd
import  numpy    as np


# TODO: factor out into file feature.py
class FeatureInfo(object):
    def __init__(self):
        # name of variable (col header)
        self.name = ''
        # categorical/quantitative
        self.statType = ''
        # data type
        self.dataType = ''


class Frame(object):
    def __init__(self):
        self._df = None

    def loadCsv(self, path):
        try:
            self._df = pd.read_csv(path)
            return either.Right('ok')
        except:
            return either.Left('failed to loadCsv')

    def getFrame(self):
        if self._df is None:
            return either.Left('no frame loaded')
        else:
            return either.Right(self._df)
