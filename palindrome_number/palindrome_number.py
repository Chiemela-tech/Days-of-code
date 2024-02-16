# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        p = str(x)
        return p == p[::-1]
    

# Example usage:
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(135))

# Follow up: Could you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # Initialize variables
        reversed_num = 0
        original_x = x
        
        # Reverse the integer
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        # Check if the reversed integer is equal to the original
        return original_x == reversed_num