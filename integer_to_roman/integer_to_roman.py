class Solution:
    def intToRoman(self, num: int) -> str:
        roman_values = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        
        roman_numeral = ""
        # Iterate through the Roman numeral values in reverse order
        for value in sorted(roman_values.keys(), reverse=True):
            # Repeat the current Roman numeral symbol while its value fits into the number
            while num >= value:
                roman_numeral += roman_values[value]
                num -= value
        return roman_numeral

# Example usage:
solution = Solution()
print(solution.intToRoman(3549))