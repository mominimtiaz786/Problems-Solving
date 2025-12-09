from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjancy_list = defaultdict(list)

        for u, v, w in times:
            adjancy_list[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # min-heap: (current_distance, node)
        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)

            # If we already found a better path, skip this outdated one
            if d > dist[node]:
                continue

            # Relax edges
            for neighbor, distance in adjancy_list[node]:
                new_dist = d + distance
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (dist[neighbor], neighbor))


        max_dist = max(dist[1:])

        return max_dist if max_dist < float('inf') else -1
