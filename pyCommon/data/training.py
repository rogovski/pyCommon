from    ..either                    import core             as either
from    sklearn.feature_extraction  import DictVectorizer
from    sklearn                     import preprocessing


class RegressionTrainingSet(object):
    '''
    training set for a regression model

    '''

    def __init__(self,
                 predictors  = None,
                 responder   = None):
        '''
        initialize
        '''
        self.setType    = 'REGRESSION'
        self.vec        = DictVectorizer()
        self.predictors = predictors
        self.responder  = responder
        self.X          = None
        self.y          = None

    def loadData(self,
                 predictorData,
                 responderData,
                 sparse=False):
        '''
        load actual data of training set (as opposed to info)
        '''
        try:
            if sparse:
                self.X = self.vec.fit_transform(predictorData)
            else:
                self.X = self.vec.fit_transform(predictorData).toarray()
            self.y = responderData
            return either.Right('ok')
        except:
            return either.Left('failed to load training set')


class ClassificationTrainingSet(object):
    '''
    training set for a classification model

    predictors : [string]
    responder  : string
    '''

    def __init__(self,
                 predictors  = None,
                 responder   = None):
        '''
        initialize
        '''
        self.setType    = 'CLASSIFICATION'
        self.vec        = DictVectorizer()
        self.le         = preprocessing.LabelEncoder()
        self.predictors = predictors
        self.responder  = responder
        self.X          = None
        self.y          = None

    def loadData(self,
                 predictorData,
                 responderData,
                 sparse=False):
        '''
        load actual data of training set (as opposed to info)

        predictorData : [{ ... }]
        responderData : numpy.array
        '''
        try:
            if sparse:
                self.X = self.vec.fit_transform(predictorData)
            else:
                self.X = self.vec.fit_transform(predictorData).toarray()
            self.y = self.le.fit_transform(responderData)
            return either.Right('ok')
        except:
            return either.Left('failed to load training set')
