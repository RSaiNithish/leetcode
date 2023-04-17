'''
1. Two Sum
 - Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.
 - You may assume that each input would have exactly one solution, and you may 
 not use the same element twice.

What we need to do:
    - We need to return indices of values that adds up to the target value.
    - Since we are given an assumption the problem further simplifies, that 
    is we need to check and return only two indices
    
Solution Logic:
    - Pick a value at an index and sum it up by pairing it with rest of the elements 
    in the list to check the sum is equal to target
    - Iterate through the list using two different itterators
    - Check if sum of the value at the indices adds up to the target
    - Return the indices
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if target-nums[i] in map.keys():
                return [map.get(target-nums[i]),i]
            else:
                map[nums[i]]=i
        
