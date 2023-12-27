class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        } 
        stack = []

        for i in s:

            # Find key using value
            key = ''.join([key for key, val in symbols.items() if val == i])

            if i in symbols.keys():
                stack.append(i)
            elif((not(stack)) or (stack.pop() != key)):
                return False

        return not(stack)