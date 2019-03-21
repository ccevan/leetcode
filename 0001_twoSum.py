class Solution:
    def twoSum(self, nums, target):
        """
        两数之和
        :param nums: 整数列表
        :param target: 目标值
        :return: 符合条件下表列表
        """
        hash_map = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hash_map:
                return [hash_map[another_num], index]
            hash_map[num] = index
        return None