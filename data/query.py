from    ..either                    import core as either
import  pandas                      as pd
import  numpy                       as np
import  matplotlib.pyplot           as plt
from    mpl_toolkits.mplot3d        import Axes3D


# filter values in a dataframe, e.g. "where a=x and b=y ..."
def dfFilter(df, query):
    try:
        return either.Right(df.query(query))
    except:
        return either.Left('failed to execute query')

# projection on dataframe, e.g. "select a,b,c from ..."
def dfProject(df, items):
    try:
        return either.Right(df.loc[:,items])
    except:
        return either.Left('failed to execute projection')

# groupby on a dataframe
def dfGroupBy(df, items):
    try:
        return either.Right(df.groupby(items))
    except:
        return either.Left('failed to execute groupby')

# apply aggregate to grouped dataframe
def dfAggregate(df, fn):
    try:
        return either.Right(df.aggregate(fn))
    except:
        return either.Left('failed to execute aggregation')
