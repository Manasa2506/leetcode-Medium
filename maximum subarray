class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur,m=0,-inf
        for c in nums:
            cur=max(c,cur+c)
            m=max(m,cur)
        return m
