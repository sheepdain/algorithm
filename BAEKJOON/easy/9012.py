n=int(input())
for _ in range(n):
    s=input().strip()
    stack=[]
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(i) # 짝이 안맞는 ')'가 들어온 경우
                break
    if stack:
        print("NO")
    else:
        print("YES")

# cnt보다 stack이 더 빠르다. stack은 append, pop이 O(1)이라서. cnt는 cnt+=1, cnt-=1이 O(1)인데도.