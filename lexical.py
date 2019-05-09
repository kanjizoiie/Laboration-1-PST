

class lexical:
    def __init__(self, parsestring):
        self.parsestring = parsestring
        self.tokenlist = []
        self.NON_DUPLICATES = ['+', '*']
        self.analyse()

    def analyse(self):
        #Read the string into a list
        for char in self.parsestring:
            self.tokenlist.append(char)
        #Remove all whitespaces in the list
        self.tokenlist = [value for value in self.tokenlist if value != " "]
        #Check for duplicate signs
        for char in self.NON_DUPLICATES:
            prev_token = 0
            for token in self.tokenlist:
                if prev_token == char and token == char:
                    raise Exception('You cannot have repeating ' + char + ' characters in a row.')
                prev_token = token


    def getTokenList(self):
        return self.tokenlist


