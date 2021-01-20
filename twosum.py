# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i =0
        twosum_list=[]
        while i < len(nums):
            j = 1
            while j <= len(nums) -i -1:
                if nums[i]+nums[i+j]==target:
                    twosum_list.append(i)
                    twosum_list.append(i+j)
                j=j+1
            i = i+1
        return twosum_list
