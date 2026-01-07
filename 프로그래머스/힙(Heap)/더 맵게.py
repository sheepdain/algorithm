def solution(scoville, K):
    answer = 0
    import heapq
    heapq.heapify(scoville)
    while scoville[0]<K and len(scoville)>1:
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer+=1

    return answer

print (solution([1, 2, 3, 9, 10, 12],7))