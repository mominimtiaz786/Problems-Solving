class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)
        skill = sorted(skill)

        skillsum = skill[0] + skill[-1]
        l,r = 0, N-1
        chemistry=0
        while l<r:
            if skill[l] + skill[r] == skillsum:
                chemistry+=(skill[l]*skill[r])
                l+=1
                r-=1
            else:
                return -1
        

        return chemistry
