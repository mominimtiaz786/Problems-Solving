class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)

        visited = {0}
        q = [0]

        while q:
            room = q.pop(0)

            rooms_unlocked = rooms[room]

            for c_room in rooms_unlocked:
                if c_room not in visited:
                    q.append(c_room)
                
                visited.add(c_room)
        
        return N == len(visited)