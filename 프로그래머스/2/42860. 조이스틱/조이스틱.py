def solution(name):
    n=len(name)
    answer = 0
    for a in name:
        answer+=min(ord(a)-ord("A"), ord("Z")-ord(a)+1)

    # 커서 이동 최소값
    move=n-1
    for i in range(n):
        next_idx=i+1
        while next_idx<n and name[next_idx]=="A":
            next_idx+=1
        move=min(move, 2*i+(n-next_idx), i+2*(n-next_idx))

    return answer+move