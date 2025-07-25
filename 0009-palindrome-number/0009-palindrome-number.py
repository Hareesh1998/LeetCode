class Solution:
    def isPalindrome(self, number: int) -> bool:
        # Negative numbers and numbers that end with 0 (and are not 0 itself) 
        # cannot be palindromes
        if number < 0 or (number != 0 and number % 10 == 0):
            return False
      
        reversed_half = 0
        # Build the reversed half of the number to reduce the number of operations
        while reversed_half < number:
            reversed_half = reversed_half * 10 + number % 10
            number //= 10
          
        # The number is a palindrome if it is the same as the reversed half or 
        # the same as the reversed half without the last digit (for odd-length numbers)
        return number == reversed_half or number == reversed_half // 10