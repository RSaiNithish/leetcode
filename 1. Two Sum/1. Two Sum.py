'''
 1. Two Sum
 - Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.
 - You may assume that each input would have exactly one solution, and you may 
 not use the same element twice.

What we need to do:
    - We need to return indices of values that adds up to the target value.
    - Since we are given an assumption the problem further simplifies, that 
    is there exist a solution.
    
Solution Logic:
    - Since we know that there exists a unique solution
    - We can pick an element and check if it's counterpart(target - element) is present in dictionary.
    - If we come accross an element whose counterpart is present in the dictionary then return the the two elements
    - Else add the {element,index} to the dictionary
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if target-nums[i] in map.keys():
                return [map.get(target-nums[i]),i]
            else:
                map[nums[i]]=i
        
