class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x1, y1 in points:
            dis = x1**2 + y1**2
            heapq.heappush(heap, (-dis, [x1, y1]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for dis, point in heap]
                
        
