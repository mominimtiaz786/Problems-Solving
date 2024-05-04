class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        N = len(people)
        
        l,r = 0, N-1
        boats = 0
        while l <= r:
            remLimit = limit
            cap = 2
            while l <= r and people[r] <= remLimit and cap:
                remLimit-=people[r]
                r-=1
                cap-=1
            
            while l <= r and people[l] <= remLimit and cap:
                remLimit-=people[l]
                l+=1
                cap-=1

            boats+=1

        return boats