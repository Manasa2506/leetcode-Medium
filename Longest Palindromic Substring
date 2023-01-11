class Solution(object):
    def longestPalindrome(self, s):
        l=len(s)
        if l==1:
            return s
        for i in range(l):
            for j in range(i+1):
                x=s[j:(l-i+j)]
                if x==x[::-1]:
                    return x
        return False
