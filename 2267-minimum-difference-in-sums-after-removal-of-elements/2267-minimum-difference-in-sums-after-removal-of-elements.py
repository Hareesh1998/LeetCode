from heapq import heappush, heappop

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total_elements = len(nums)
        one_third_length = total_elements // 3  

        prefix_sum = 0
        max_heap_prefix = [] 
        prefix_sums = [0] * (total_elements + 1)  
        for i in range(1, one_third_length * 2 + 1):
            prefix_sum += nums[i - 1]
            heappush(max_heap_prefix, -nums[i - 1])  
            if len(max_heap_prefix) > one_third_length:
                prefix_sum += heappop(max_heap_prefix)  
            prefix_sums[i] = prefix_sum
      
        suffix_sum = 0
        min_heap_suffix = []  
        suffix_sums = [0] * (total_elements + 1) 

        for i in range(total_elements, one_third_length - 1, -1):
            suffix_sum += nums[i - 1]
            heappush(min_heap_suffix, nums[i - 1])
            if len(min_heap_suffix) > one_third_length:
                suffix_sum -= heappop(min_heap_suffix)  
            suffix_sums[i] = suffix_sum
      

        min_difference = float('inf')  
        for i in range(one_third_length, one_third_length * 2 + 1):
            min_difference = min(min_difference, prefix_sums[i] - suffix_sums[i + 1]) 
        return min_difference
