from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = deque([0])
        
        while stack:
            room = stack.popleft()
            visited.add(room)
            
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
                    
        return len(visited) == len(rooms)