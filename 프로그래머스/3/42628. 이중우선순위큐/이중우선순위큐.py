import heapq

def solution(operations):
    answer = [0, 0]
    num_dict = {}
    max_heap = []
    min_heap = []
    
    for op in operations:
        command, num = op.split()
        num = int(num)
        
        if command == 'I':
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
            num_dict[num] = num_dict.get(num, 0) + 1
        else:
            if num == 1:
                while max_heap:
                    target = -heapq.heappop(max_heap)
                    if num_dict.get(target, 0) > 0:
                        num_dict[target] -= 1
                        break
            else:
                while min_heap:
                    target = heapq.heappop(min_heap)
                    if num_dict.get(target, 0) > 0:
                        num_dict[target] -= 1
                        break

    while max_heap:
        target = -heapq.heappop(max_heap)
        if num_dict.get(target, 0) > 0:
            answer[0] = target
            heapq.heappush(max_heap, -target) 
            break
            
    while min_heap:
        target = heapq.heappop(min_heap)
        if num_dict.get(target, 0) > 0:
            answer[1] = target
            break

    return answer