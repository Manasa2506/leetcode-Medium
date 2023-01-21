class Solution(object):
    def fractionToDecimal(self, n,d):
        if n%d==0: return str(n//d)
        p,q,r,s,m=abs(n),abs(d),abs(n)%abs(d),'',{}
        while r and r not in m: m[r],r,s=len(s),r*10%q,s+str(r*10//q)
        return ("" if (n>0)==(d>0) else '-') + str(p//q)+ '.'+(s[:m[r]]+'('+s[m[r]:]+')' if r else s)
