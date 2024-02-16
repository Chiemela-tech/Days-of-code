# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        p = str(x)
        return p == p[::-1]
    

# Example usage:
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(135))