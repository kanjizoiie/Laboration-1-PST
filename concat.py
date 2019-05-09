from expression import expression as exp
class concat(exp):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.debug()
    
    def debug(self):
        print(self)

    def __str__(self):
        return str(self.lhs) + ':' + str(self.rhs)
        
    def eval(self, stringinput):
        try:
            left = self.lhs.eval(stringinput)
            stringinput = stringinput[len(left):]
            right = self.rhs.eval(stringinput)
            if not left or not right:
                return False
            else:
                return left + right
        except:
            return False