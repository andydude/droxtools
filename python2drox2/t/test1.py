"""docs"""

@good
class DontUseThis (SuperClass):
    """This is a test, don't use it... ever"""

    @bad(what)
    def __init__(self, what, are_these, extra, parameters, doing, here):
        """ function docs """
        pass

    def __del__(self):
        a = 5
        a += 2
        a /= 10
        pass
