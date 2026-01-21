def solution(word):
    words=['A', 'E', 'I', 'O', 'U']
    cnt=0
    answer=0

    def dfs(next_w):
        nonlocal cnt, answer
        if len(next_w)==5 or answer>0:
            return

        for w in words:
            next_word=next_w+w
            cnt+=1
            if next_word==word:
                answer=cnt
                break
            dfs(next_word)
            if answer > 0: return
    dfs('')

    return answer

print(solution("EIO"))