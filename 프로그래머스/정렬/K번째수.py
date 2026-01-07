# def solution(array, commands):
#     answer = []
#     for command in commands:
#         ans=array[command[0]-1:command[1]]
#         ans.sort()
#         answer.append(ans[command[2]-1])
#     return answer

def solution(array, commands):
    answer=[]
    for i,j,k in commands:
        ans=array[i-1:j]

        import heapq
        heap=[]
        for num in ans:
            heapq.heappush(heap, -num)
            if len(heap)>k:
                heapq.heappop(heap)

        answer.append(-heapq.heappop(heap))
    return answer
            
print (solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))