class Solution:
    def twoSum(self, nums, target):

        hash_map = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hash_map:
                return [hash_map[another_num], index]
            hash_map[num] = index
        return None