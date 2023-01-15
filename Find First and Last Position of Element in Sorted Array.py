class Solution(object):
    def searchRange(self, nums, target):
        def search(x):
            left=0
            right=len(nums)
            while left<right:
                mid=(left+right)//2
                if nums[mid]<x:
                    left=mid+1
                else:
                    right=mid
            return left
        left=search(target)
        right=search(target+1)-1
        if left<=right:
            return [left,right]
        return [-1,-1]
