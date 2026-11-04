import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:

        n = len(tasks)
        sortedTask = []
        min_heap = []
        for i in range(n):
            start_time = tasks[i][0]
            processing_time = tasks[i][1]
            index = i
            sortedTask.append([start_time, processing_time, index])
        sortedTask.sort()
        result = []
        curr_time = 0
        idx = 0
        while idx < n or min_heap:
            if not min_heap and curr_time < sortedTask[idx][0]:
                curr_time = sortedTask[idx][0]
            while idx < n and sortedTask[idx][0] <= curr_time:
                heapq.heappush(min_heap, (sortedTask[idx][1], sortedTask[idx][2]))
                idx += 1
            curr_task = heapq.heappop(min_heap)
            curr_time += curr_task[0]
            result.append(curr_task[1])

        return result