class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)
        skill = sorted(skill)

        skillsum = skill[0] + skill[-1]
        l,r = 0, N-1
        teams = []
        while l<r:
            if skill[l] + skill[r] == skillsum:
                teams.append((skill[l],skill[r]))
                l+=1
                r-=1
            else:
                return -1
        

        return sum([t[0]*t[1] for t in teams])
