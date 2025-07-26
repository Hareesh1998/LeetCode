from heapq import heapify, heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
      
        busy_rooms_heap = []
        idle_rooms_heap = list(range(n))
        heapify(idle_rooms_heap)
      
        meeting_count = [0] * n
      
        for start_time, end_time in meetings:
           
            while busy_rooms_heap and busy_rooms_heap[0][0] <= start_time:
                room_index = heappop(busy_rooms_heap)[1]
                heappush(idle_rooms_heap, room_index)
          
            if idle_rooms_heap:
                room_index = heappop(idle_rooms_heap)
                meeting_count[room_index] += 1
                heappush(busy_rooms_heap, (end_time, room_index))
            else:
                earliest_end, room_index = heappop(busy_rooms_heap)
                meeting_count[room_index] += 1
              
               
                heappush(busy_rooms_heap, (earliest_end + end_time - start_time, room_index))
      
        most_booked_room = 0
        for i, count in enumerate(meeting_count):
            if meeting_count[most_booked_room] < count:
                most_booked_room = i
              
        return most_booked_room


solution = Solution()

n = 2
meetings = [[0, 10], [0, 5], [10, 15]]
most_booked = solution.mostBooked(n, meetings)
print("The most booked room is:", most_booked)