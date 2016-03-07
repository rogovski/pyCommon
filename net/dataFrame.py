import  pyCommon.either.core        as either
import  pyCommon.data.query         as query
import  pandas                      as pd
import  numpy                       as np
import  time

class dataFrame(object):
  def __init__(self):
    self._df = None

  def loadCsv(self, path):
    time.sleep(10)
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
