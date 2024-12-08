class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        result = [0] * n 
        adj_list = [[] for i in range(n+1)]

        for i, j in paths: 
            adj_list[i].append(j)
            adj_list[j].append(i)

        if not adj_list:
            return [(n%4)+1 for i in range(n)]

        possible_flowers = [1,2,3,4]
        for i in range(1, n+1):
            if result[i-1] == 0:
                neighbours = adj_list[i] 
                assigned = []
                for j in neighbours:
                    if result[j-1] != 0:
                        assigned.append(result[j-1])
                # O(n)
                for k in possible_flowers:
                    if k not in assigned:
                        result[i-1] = k
                        break

        # O(v+ve)
        return result


            


        