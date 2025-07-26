from collections import defaultdict
from math import inf

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
    
        def dfs(node, parent, exclude_node):
            result = nums[node]
            for neighbor in graph[node]:
                if neighbor != parent and neighbor != exclude_node:
                    result ^= dfs(neighbor, node, exclude_node)
            return result

        def dfs_with_score(node, parent, exclude_node):
            nonlocal total, subtree_xor, min_score
            result = nums[node]
            for neighbor in graph[node]:
                if neighbor != parent and neighbor != exclude_node:
                    subtree_result = dfs_with_score(neighbor, node, exclude_node)
                    result ^= subtree_result
                    remaining_xor = subtree_xor ^ subtree_result
                    rest_of_tree_xor = total ^ subtree_xor
                    max_xor = max(subtree_result, remaining_xor, rest_of_tree_xor)
                    min_xor = min(subtree_result, remaining_xor, rest_of_tree_xor)
                    score_difference = max_xor - min_xor
                    min_score = min(min_score, score_difference)
            return result

        graph = defaultdict(list)
        for start_node, end_node in edges:
            graph[start_node].append(end_node)
            graph[end_node].append(start_node)

        total = 0
        for value in nums:
            total ^= value

        min_score = inf

        for i in range(len(nums)):
            for j in graph[i]:
             
                subtree_xor = dfs(i, -1, j)
               
                dfs_with_score(i, -1, j)
              
        return min_score
