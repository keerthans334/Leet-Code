class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        if x/10==0:
            return True
        reversednum=(int(str(x)[::-1]))
        if x==reversednum:
            return True
        else:
            return False

        