class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        comp_dict = {}
        for i in range(len(nums)):
            if nums[i] in comp_dic:
                return [comp_dic[nums[i]], i]
            else:
                comp_dict[target - nums[i]] = i
