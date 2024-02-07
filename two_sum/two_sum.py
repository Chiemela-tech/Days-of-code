from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of elements
        num_dict = {}
         # Iterate through the array
        for i, num in enumerate(nums):
    # Calculate the complement needed for the current number to reach the target
            complement = target - num
         # Check if the complement exists in the dictionary
            if complement in num_dict:
             # If found, return the indices of the two numbers
                return [num_dict[complement], i]
             # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = i
        # If no solution is found, return an empty list
        return []
    

nums = [2, 7, 11, 15]
target = 9
summer = Solution()
print(summer.twoSum(nums, target))  