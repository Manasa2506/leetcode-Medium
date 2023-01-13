class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=-1 if (dividend>=0 and divisor<0) or (dividend <0 and divisor>=0) else 1
        dividend=abs(dividend)
        divisor=abs(divisor)
        res=len(range(0,dividend-divisor+1,divisor))
        if sign==-1:
            res=-res
        mLimit=-(2**31)
        pLimit=(2**31)-1
        res=min(max(res,mLimit),pLimit)
        return res 
