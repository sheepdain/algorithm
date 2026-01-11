def solution(numbers):
    used=[False] * len(numbers)
    nums=set()
    
    def dfs(current):
        if current:
            nums.add(int(current))
            
        for i in range(len(numbers)):
            if not used[i]:
                used[i]=True
                dfs(current+numbers[i])
                used[i]=False
    dfs("")
    
    # 소수 개수 세기
    answer = 0
    for num in nums:
        if prime(num):
            answer+=1
    return answer

def prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n%i==0:
            return False
    return True