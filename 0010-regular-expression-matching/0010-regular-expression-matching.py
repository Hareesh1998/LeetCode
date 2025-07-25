class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        text_length, pattern_length = len(text), len(pattern)

        dp = [[False] * (pattern_length + 1) for _ in range(text_length + 1)]

        dp[0][0] = True

        for i in range(text_length + 1):
            for j in range(1, pattern_length + 1):
                if pattern[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if i > 0 and (pattern[j - 2] == "." or text[i - 1] == pattern[j - 2]):
                        dp[i][j] |= dp[i - 1][j]
                elif i > 0 and (pattern[j - 1] == "." or text[i - 1] == pattern[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[text_length][pattern_length]
