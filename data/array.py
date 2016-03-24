import numpy as np


def maprows(f, a):
    '''
    map f over the rows of a
    '''
    return np.array(map(f, a))


def mapcols(f, a):
    '''
    map f over the columns of a
    '''
    return maprows(f, a.T).T