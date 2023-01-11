class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        l=[]
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:#check duplicates
                continue#skip if duplicate
            j=i+1
            k=len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s>0:
                    k-=1
                elif s<0:
                    j+=1
                else:
                    l.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j-1]==nums[j] and j<k:
                        j+=1
        return l
