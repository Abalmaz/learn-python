class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums)-1
        while first<=last:
            midpoint = first+(last-first)//2
            if nums[midpoint] == target:
                break
            else:
                if target < nums[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        if target > nums[midpoint]:
            midpoint += 1
        return midpoint
