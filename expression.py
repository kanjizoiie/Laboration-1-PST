class expression:

    """This is a class that is used to create the hierarcy
    """
    def __init__(self, inputstring):
        self.expression = inputstring
        self.debug()

    def __str__(self):
        return str(self.expression)

    def debug(self):
        print(self)
        
    def eval(self, c):
        if (self.expression == '.'):
            return c[0]
        elif (self.expression == c[0]):
            return c[0]
        else:
            return False
