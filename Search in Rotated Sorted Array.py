class Solution(object):
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        return -1
