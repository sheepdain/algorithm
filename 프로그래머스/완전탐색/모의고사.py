def solution(answers):
    result=[0,0,0]
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i]==a[i%5]:
            result[0]+=1
        if answers[i]==b[i%8]:
            result[1]+=1
        if answers[i]==c[i%10]:
            result[2]+=1
    answer = []
    for j in range(3):
        ans_cnt=max(result)
        if result[j]==ans_cnt:
            answer.append(j+1)
    return answer

res=solution([1,2,3,4,5])
print (res)