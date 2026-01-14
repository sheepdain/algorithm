def solution(n, lost, reserve):
    los=set(lost)-set(reserve)
    res=set(reserve)-set(lost)
    cnt=len(los)
    for l in los:
        for r in res:
            if abs(l-r)==1:
                res.remove(r)
                cnt-=1
                break

    answer = n-cnt
    return answer