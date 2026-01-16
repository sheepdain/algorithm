def solution(routes):
    routes_s=sorted(routes, key=lambda x:x[1])
    answer = 0
    camera = -30001
    for start, end in routes_s:
        if not start <= camera <= end:
            answer += 1
            camera = end
    
    return answer