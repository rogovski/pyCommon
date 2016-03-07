
# base either object
class Either(object):
    def __init__(self, name):
        self.name = name

# represents a failure with a message
class Left(Either):
    def __init__(self, val):
        super(Left, self).__init__('Left')
        self.val = val

    def __str__(self):
        return 'Left: %s' % str(self.val)

# represents a success with a value
class Right(Either):
    def __init__(self, val):
        super(Right, self).__init__('Right')
        self.val = val

    def __str__(self):
        return 'Right: %s' % str(self.val)

# represents pending with a message
class Pending(Either):
    def __init__(self, val):
        super(Pending, self).__init__('Pending')
        self.val = val

    def __str__(self):
        return 'Pending: %s' % str(self.val)

# reverse composition. see haskell <=<
def pipe(*args):
    arglen = len(args)

    if arglen < 2:
        raise Exception('pipe: takes 2 or more args')

    def go(x):
        eitherval = args[0](x)
        if type(eitherval) is Left:
          return eitherval

        if type(eitherval) is Pending:
          return eitherval

        for i in range(1,arglen):
            eitherval = args[i](eitherval.val)
            if type(eitherval) is Left:
                break
            if type(eitherval) is Pending:
                break

        return eitherval

    return go
