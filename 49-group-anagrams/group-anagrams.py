class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
    # hash map
    # nat tan
    # ant -> [tan, nat]

    # groups 

    # strs = ["eat","tea","tan","ate","nat","bat"]
    
    # aet - grp[0]
    # eat, tea -> key 0
    # tan -> ant -> key ant
    # ate -> aet -> key tea

        groups = {}

        # eat, tea, ate
        # [a,b,c...], [0101], 
        # one loop for computing arrays
        # one loop for [0, 1, 0], [0, 1, 0], [1, 0, 0], [1] 

        for i in strs: # number of words
            # print("word: ", strs[i])
            key = ''.join(sorted(i)) #sorting length of string -> k log k
            # check if key exists in group
            if key not in groups:
                print("key is in group")
                groups[key] = []
            print("key:", key)
            groups[key].append(i)
        
        return list(groups.values())

        # 

        

        

