from    ..either                    import core as either
import  pandas                      as pd
import  numpy                       as np
import  matplotlib.pyplot           as plt
from    mpl_toolkits.mplot3d        import Axes3D

# get names of features
def getDimensionNames(df):
    return df.columns.values

# make an educated guess about the type of
# the dimension (Categorical/Quantitative) (Int, Double, etc)
# TODO: make some use of df.sample(n)
def getDimensionType(df, name):
    return either.Left('NOT IMPLEMENTED')

# get the list of unique categories of a feature
def getUniqueCategories(df, name):
    if name not in df.columns: 
        return either.Left('provided name not found')
    else:
        return either.Right(
            np.unique(df[name].values.ravel())
        )

# filter values in a dataframe, e.g. "where a=x and b=y ..."
def rFilter(df, query):
    try:
        return either.Right(df.query(query))
    except:
        return either.Left('failed to execute query')

# projection on dataframe, e.g. "select a,b,c from ..."
def rProject(df, items):
    try:
        return either.Right(df.loc[:,items])
    except:
        return either.Left('failed to execute projection')

# groupby on a dataframe
def rGroupBy(df, items):
    try:
        return either.Right(df.groupby(items))
    except:
        return either.Left('failed to execute groupby')

# apply aggregate to grouped dataframe
def rAggregate(df, fn):
    try:
        return either.Right(df.aggregate(fn))
    except:
        return either.Left('failed to execute aggregation')
