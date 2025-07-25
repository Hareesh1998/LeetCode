class Solution:
    def myAtoi(self, str: str) -> int:
        # Return 0 if string is empty
        if not str:
            return 0

        length_of_string = len(str)
        index = 0

        # Skip leading whitespaces
        while index < length_of_string and str[index] == ' ':
            index += 1

        # After skipping whitespaces, if we're at the end it means it's an empty string
        if index == length_of_string:
            return 0

        # Check if we have a sign, and set the sign accordingly
        sign = -1 if str[index] == '-' else 1
        if str[index] in ['-', '+']:  # skip the sign for next calculations
            index += 1

        result = 0
        max_safe_int = (2 ** 31 - 1) // 10  # Precomputed to avoid overflow

        while index < length_of_string:
            # If the current character is not a digit, break from loop
            if not str[index].isdigit():
                break

            digit = int(str[index])

            # Check for overflow cases
            if result > max_safe_int or (result == max_safe_int and digit > 7):
                return 2 ** 31 - 1 if sign == 1 else -2 ** 31  # Clamp to INT_MIN or INT_MAX

            # Append current digit to result
            result = result * 10 + digit
            index += 1

        # Apply sign and return final result
        return sign * result