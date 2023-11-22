class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(list(reversed(list(str(x)))) == list(str(x))):
            return True
        else:
            return False