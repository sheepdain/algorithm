def solution(citations):
    citations.sort(reverse=True)
    for i in range (len(citations)):
        if citations[i]<i+1:
            answer=citations[i-1]
            break
            
    return answer