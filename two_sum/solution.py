class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        processed = {}
        for i in range(0, len(nums)):
            if target-nums[i] in processed:
                return [processed[target-nums[i]],i]
            processed[nums[i]]=i
