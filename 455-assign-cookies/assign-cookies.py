class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        N_s = len(s)
        G_s = len(g)
        if not N_s: return 0

        s.sort()
        g.sort()

        children_content = 0

        i,j = 0,0

        found = True
        while found and i < G_s:
            found = False
            req = g[i]
            while j< N_s:
                if req <= s[j]:
                    found=True
                    children_content+=1
                    j+=1
                    break
                j+=1
            i+=1
        


        return children_content
        




        