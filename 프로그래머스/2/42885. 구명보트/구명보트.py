def solution(people, limit):
    people.sort()
    start, end=0, len(people)-1
    answer = end+1
    while start<end:
        if people[end]+people[start]<=limit:
            start+=1
            answer-=1
        end-=1
    return answer