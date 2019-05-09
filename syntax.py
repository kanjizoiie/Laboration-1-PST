from expression import expression
from orop import orop
from concat import concat
from para import para
from catch import catch
from rep import rep


class syntax:
    def __init__(self, tokens):
        self.tokens = tokens
        self.currToken = tokens[0]
        self.prevToken = ''

    def next(self):
        self.tokens = self.tokens[1:]
        self.currToken = self.tokens[0] if len(self.tokens) > 0 else None
    
    def evaluate(self, string, tree):
        while True:
            evaluation = tree.eval(string)
            if not(evaluation):
                string = string[1:]
                if(len(string) == 0):
                    raise Exception('The pattern matcher found nothing!')
            else:
                return evaluation

    def parse_catch(self):
        left = self.parse_or()
        if left:
            if self.currToken == '<':
                self.next()
                middle = self.parse_or()
                if self.currToken == '>':
                    self.next()
                    right = self.parse_or()
                    if(not(right)):
                        raise Exception('Could not parse to the right side of a catch.\n Catch requires an something to the right of it.')
                    return catch(left, middle, right)
                else:
                    raise Exception('Catch clause is malformed, there is a \'>\' symbol missing')
            else:
                return left
        else:
            raise Exception('Could not parse to the left side of a catch.\n Catch requires an something to the right of it.')

    def parse_or(self):
        left = self.parse_concat()
        if left:
            if self.currToken == '+':
                self.next()
                right = self.parse_or()
                if right:
                    return orop(left, right)
                else:
                    raise Exception('A \'+\' is malformed')
            else:
                return left
        else:
            return None



    def parse_concat(self):
        left = self.parse_rep()
        if left:
            right = self.parse_concat()
            if right:
                return concat(left, right)
            elif left:
                return left
            else:
                return None

    def parse_rep(self):
        inner = self.parse_term()
        if self.currToken == '*':
            self.next()
            return rep(inner)
        else:
            return inner



    def parse_term(self):
        try:
            if self.currToken.isalpha() or self.currToken == '.':
                return self.parse_char()
            elif self.currToken == '(':
                return self.parse_nested()
        except:
            return None



    def parse_nested(self):
        self.next()
        ret = para(self.parse_or())
        self.next()
        return ret

    def parse_char(self):
        ret = expression(self.currToken)
        self.next()
        return ret
