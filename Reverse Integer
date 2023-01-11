class Solution(object):
    def reverse(self, x):
        def signC(x):
            if x>=0:
                return 1
            else:
                return -1
        sign=signC(x)
        n=str(abs(x))
        reverse=n[::-1]
        num= sign*int(reverse)
        if abs(num)>(2**31)-1:
            return 0
        else:
            return num
