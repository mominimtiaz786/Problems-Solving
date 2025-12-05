class Solution:
    def watchedVideosByFriends(
        self, watchedVideos: List[List[str]], 
        friends: List[List[int]], 
        id: int, level: int) -> List[str]:

        if not friends:   return []
        
        queue = [id]
        my_set = set(queue)

        for i in range(level):
            queue_l = len(queue)
            for j in range(queue_l):
                elem_id = queue.pop(0)
                level_friends = friends[elem_id]
                for fr in level_friends:
                    if fr not in my_set:
                        my_set.add(fr)
                        queue.append(fr)
                
        
        ans=[]
        for fr in queue:
            ans+=watchedVideos[fr]

        freq = defaultdict(int)
        for v in ans:   
            freq[v]+=1

        ans = list(set(ans))
        ans.sort()
        ans.sort(key= lambda x : freq[x])
        return ans


