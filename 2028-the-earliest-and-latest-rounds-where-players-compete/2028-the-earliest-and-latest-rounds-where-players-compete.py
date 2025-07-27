from typing import List
import functools
import math

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        
        @functools.lru_cache(None)
        def dp(left_index: int, right_index: int, num_players: int) -> List[int]:
            
          
            
            if left_index == right_index:
                return [1, 1]

           
            if left_index > right_index:
                return dp(right_index, left_index, num_players)

           
            earliest_round = math.inf
            latest_round = -math.inf

          
            for i in range(1, left_index + 1):
                for j in range(left_index - i + 1, right_index - i + 1):
                    if not left_index + right_index - num_players // 2 <= i + j <= (num_players + 1) // 2:
                        continue
                   
                    new_earliest, new_latest = dp(i, j, (num_players + 1) // 2)
                    earliest_round = min(earliest_round, new_earliest + 1)
                    latest_round = max(latest_round, new_latest + 1)

            return [earliest_round, latest_round]

        
        return dp(firstPlayer, n - secondPlayer + 1, n)