import lexical
import syntax
import sys

try:
    pattern = sys.argv[1]
    string = sys.argv[2]
except IndexError:
    raise IndexError('You need to give this program two arguments. \n'
                     'Ex: python main.py *pattern* *string to match*')

print('Current pattern: ' + pattern)
print('Current string: ' + string)

lex = lexical.lexical(pattern)
syn = syntax.syntax(lex.getTokenList())
tree = syn.parse_catch()
print('TRYING TO MATCH')
print('Found:' + syn.evaluate(string, tree))