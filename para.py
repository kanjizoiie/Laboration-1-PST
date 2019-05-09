from expression import expression as exp
class para(exp):
    def __init__(self, expression):
        self.expression = expression
        self.debug()

    def __str__(self):
        return '(' + str(self.expression) + ')'

    def debug(self):
        print(self)

    def eval(self, stringinput):
        evaluated = self.expression.eval(stringinput)
        return evaluated