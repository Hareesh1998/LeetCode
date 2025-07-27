from typing import List  

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
      
        
        match_count = 0
        trainer_index = 0
      
        for player in players:
            
            while trainer_index < len(trainers) and trainers[trainer_index] < player:
                trainer_index += 1
              
            
            if trainer_index < len(trainers):
                match_count += 1
               
                trainer_index += 1
      
        return match_count