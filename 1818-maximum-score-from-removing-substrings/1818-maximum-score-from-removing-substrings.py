class Solution:
    def maximumGain(self, string: str, value_a: int, value_b: int) -> int:
        if value_a < value_b:
            return self.maximumGain(string[::-1], value_b, value_a)      
        answer = 0
        stack_ab, stack_ba = [], []
        for char in string:
            if char != 'b':
                stack_ab.append(char)
            else:
                if stack_ab and stack_ab[-1] == 'a':
                    stack_ab.pop()
                    answer += value_a
                else:
                    stack_ab.append(char)
        while stack_ab:
            char = stack_ab.pop()
            if char != 'b':
                stack_ba.append(char)
            else:
                if stack_ba and stack_ba[-1] == 'a':
                    stack_ba.pop()
                    answer += value_b
                else:
                    stack_ba.append(char)
        return answer
