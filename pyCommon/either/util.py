import core as either


def failIf(cond, errMessage):
    return lambda _: either.Left(errMessage) if cond \
            else either.Right(cond)


def dictGet(key, dictionary):
    if key in dictionary:
        return either.Right(dictionary[key])
    else:
        return either.Left('key not found') 