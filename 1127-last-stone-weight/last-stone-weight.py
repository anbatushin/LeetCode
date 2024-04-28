class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, stone * (-1))
        heap_len = len(heap)
        while heap_len > 1:
            y = abs(heappop(heap))
            x = abs(heappop(heap))
            if x == y:
                heap_len -= 2
            else:
                heappush(heap, x - y)
                heap_len -= 1

        return heap[0] * (-1) if heap_len == 1 else 0
