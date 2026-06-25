class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #max heap, counting how many tasks per each element, heap that takes in task and count
        #while heap, set time pointer, from max heap, pop first, count -= 1.
        #map[time += n] = task, count
        #every iteration, heapq.heappush(map[time], heap)

        count = Counter(tasks)

        heap = []
        for task, freq in count.items():
            heapq.heappush(heap, (-freq, task))

        ma = {}
        time = 0
        while heap or ma:
            time += 1

            if time in ma:
                freq, task = ma.pop(time)
                heapq.heappush(heap, (freq, task))
            
            if heap:

                freq, task = heapq.heappop(heap)
                freq += 1
                if freq != 0:
                    ma[time + n + 1] = freq, task


        return time
            