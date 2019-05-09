from expression import expression as exp

class rep(exp):
    def __init__(self, expression):
        self.expression = expression
        self.debug()

    def debug(self):
        print(self)

    def __str__(self):
        return str(self.expression) + '*'

    def eval(self, string):
        ret = []
        while True:
            try:
                parsed = self.expression.eval(string)
            except:
                parsed = False
            if parsed:
                string = string[len(parsed):]
            else:
                break
            ret.append(parsed)
        return ''.join(ret)