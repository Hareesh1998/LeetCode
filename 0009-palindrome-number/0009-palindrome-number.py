class Solution:
    def isPalindrome(self, number: int) -> bool:

        if number < 0 or (number != 0 and number % 10 == 0):
            return False
      
        reversed_half = 0
        while reversed_half < number:
            reversed_half = reversed_half * 10 + number % 10
            number //= 10
          

        return number == reversed_half or number == reversed_half // 10