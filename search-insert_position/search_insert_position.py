from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #two pointers - left and right are initiated
        # left is initialized to the beginning of the array (0)
        left = 0

        # right is initialized to the end of the array
        right = len(nums) - 1

        #Start a binary search loop
        # This loop runs until the left pointer is less than or equal to the right pointer
        while left<= right:

            #Calculate the middle index of the current search range.
            mid = (left+right) // 2

            #Check if the value at the middle index mid is less than the target
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left

    

nums = [2, 5, 6, 9]
target = 9
summer = Solution()
print(summer.searchInsert(nums, target))  