import heapq

def solution(jobs):
    jobs.sort()

    heap = []
    time = 0
    idx = 0
    total = 0
    n = len(jobs)

    while idx < n or heap:
        while idx < n and jobs[idx][0] <= time:
            request, use = jobs[idx]
            heapq.heappush(heap, (use, request,idx))
            idx += 1

        if heap:
            use, request, num = heapq.heappop(heap)
            time += use
            total += time - request
        else:
            time = jobs[idx][0]

    return total // n
