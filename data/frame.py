from    ..either                    import core             as either
from    sklearn.feature_extraction  import DictVectorizer
import  pandas                                              as pd
import  numpy                                               as np


def _failIf(cond, errMessage):
    return lambda _: either.Left(errMessage) if cond \
            else either.Right(cond)

class Frame(object):
    def __init__(self, df=None):
        self._df                    = df
        self._views                 = {}
        self._classificationSets    = {}
        self._regressionSets        = {}

    def loadCsv(self, path):
        try:
            self._df = pd.read_csv(path)
            return either.Right('ok')
        except:
            return either.Left('failed to loadCsv')

    def loadPandas(self, df):
        self._df = df
        return either.Right('ok')

    def getFrame(self):
        if self._df is None:
            return either.Left('no frame loaded')
        else:
            return either.Right(self._df)

    def createView(self, viewName, query=[], overwrite=True):
        return either.pipe(
            _failIf(not overwrite and viewName in self._views,
                'cannot overwrite existing view'
            ),
            _failIf(type(query) is not list,
                'sub view query must be a list'
            ),
            _failIf(len(query) == 0,
                'sub view must be constructed with a query'
            ),
            lambda _: self._createViewUNSAFE(viewName, query)
        )(None)


    def createRegressionSet(self, predictors=None, responder=None, view=None):
        if self._df is None:
            return either.Left('no frame loaded')
        if predictors is None:
            return either.Left('no predictors given')
        if responder is None:
            return either.Left('no responder given')
        if view is not None and view in self._views:
            return self._views[view].asRegressionSet(predictors, responder)

        vec = DictVectorizer()
        predictorSet = self.asDictListKeep(keep=predictors).val
        predictorSet = vec.fit_transform(predictorSet).toarray()
        responderSet = self._df[responder].values
        return either.Right( (predictorSet, responderSet) )


    def createClassificationSet(self, predictors=None, responder=None, view=None):
        if self._df is None:
            return either.Left('no frame loaded')
        if predictors is None:
            return either.Left('no predictors given')
        if responder is None:
            return either.Left('no responder given')

        return either.Left('Not Implemented')


    def asDictListExclude(self, exclude=[]):
        if self._df is None:
            return either.Left('no frame loaded')

        keeps, toZip = [], []
        colVals = self._df.columns.values
        for i in np.arange(0, len(colVals)):
            if colVals[i] not in exclude:
                keeps.append(colVals[i])
                toZip.append(self._df.ix[:,i].values)

        return either.Right(
            map(lambda x: dict(zip(keeps, x)), zip(*toZip))
        )


    def asDictListKeep(self, keep=[]):
        if self._df is None:
            return either.Left('no frame loaded')

        keeps, toZip = [], []
        colVals = self._df.columns.values
        for i in np.arange(0, len(colVals)):
            if colVals[i] in keep:
                keeps.append(colVals[i])
                toZip.append(self._df.ix[:,i].values)

        return either.Right(
            map(lambda x: dict(zip(keeps, x)), zip(*toZip))
        )


    #####################################################################
    ##### UNSAFE METHODS: USED PRIMARILY AS HELPER FUNCTIONS ############
    #####################################################################


    def _createViewUNSAFE(self, viewName, query):
        qres = query[0](self._df) if len(query) == 1 \
            else either.pipe(*query)(self._df)

        if qres.name is 'Left':
            return either.Left('failed to create view')
        else:
            self._views[viewName] = Frame(qres.val)
            return either.Right('ok')


    def _asDictListExcludeUNSAFE(self, exclude):
        keeps, toZip = [], []
        colVals = self._df.columns.values
        for i in np.arange(0, len(colVals)):
            if colVals[i] not in exclude:
                keeps.append(colVals[i])
                toZip.append(self._df.ix[:,i].values)

        return either.Right(
            map(lambda x: dict(zip(keeps, x)), zip(*toZip))
        )


    def _asDictListKeepUNSAFE(self, keep):
        keeps, toZip = [], []
        colVals = self._df.columns.values
        for i in np.arange(0, len(colVals)):
            if colVals[i] in keep:
                keeps.append(colVals[i])
                toZip.append(self._df.ix[:,i].values)

        return either.Right(
            map(lambda x: dict(zip(keeps, x)), zip(*toZip))
        )