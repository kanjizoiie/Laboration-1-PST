from expression import expression as exp
class orop(exp):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.debug()
        
    def __str__(self):
        return str(self.lhs) + '+' + str(self.rhs)

    def debug(self):
        print(self)

    def eval(self, string):
        left = self.lhs.eval(string)
        right = self.rhs.eval(string)
        if (not(left)):
            evaluated = right
        elif (not(right)):
            evaluated = left
        else:
            return False   
        return evaluated
    