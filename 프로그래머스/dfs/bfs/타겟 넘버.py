def solution(numbers, target):
    answer = 0
    
    def dfs(idx, num_sum):
        nonlocal answer
        
        if idx ==len(numbers):
            if num_sum == target:
                answer += 1
            return
        
        dfs(idx+1, num_sum + numbers[idx])
        dfs(idx+1, num_sum - numbers[idx])
        
    dfs(0,0)
    return answer