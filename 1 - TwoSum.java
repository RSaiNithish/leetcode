package LeetCode;

/*
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
    - We can pick an element and check if it's counterpart(target - element) is present in a hashmap.
    - If we come accross an element whose counterpart is present in the hashmap then break out of the loop
    - Else add the element,index to the hashmap
    - Return the the two elements
 */

import java.util.HashMap;


class Solution {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int x = 0;
        int y = 0;
        for(int i = 0; i<nums.length;i++){
            x = i;
            if (map.containsKey(target - nums[i])){
                y = map.get(target-nums[i]);
                break;
            }
            map.putIfAbsent(nums[i],i);
        }
        return new int[] {y,x};
    }
}
