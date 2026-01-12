# 흐름
# target이 words에 없으면 → 0 반환
# 큐에 (현재 단어, 변환 횟수) 저장
# 방문한 단어는 다시 안 봄
# target 만나면 그때의 횟수 반환

from collections import deque

def check(x, y):
    cnt=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            cnt+=1
    return cnt==1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    n=len(words)
    visited=[False]*n
    queue = deque()
    queue.append((begin, 0))

    while queue:
        word, num=queue.popleft()
        if word==target:
            return num
        
        for i in range(n):
            if not visited[i] and check(word,words[i]):
                visited[i]=True
                queue.append((words[i],num+1))   
    
    return 0