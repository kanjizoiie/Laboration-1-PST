from expression import expression as exp

class catch(exp):
    def __init__(self, left, middle, right):
        self.left = left
        self.middle = middle
        self.right = right
        self.debug()

    def __str__(self):
        return str(self.left) + '<' + str(self.middle) + '>' + str(self.right)

    def debug(self):
        print(self)

    # If the left and right matches, evaluate the middle and then return the matched string.
    def eval(self, string):
        left_val = self.left.eval(string)
        if left_val:
            string = string[len(left_val):]
            # Evaluate from the right until we find a match
            for i in range(0, len(string)):
                right_val = self.right.eval(string[-i:])
                if right_val:
                    # Remove the amount of letters from the right which successfully matched.
                    string = string[:-i]
                    break
        if (left_val and right_val):
            return self.middle.eval(string)
        else:
            return False

