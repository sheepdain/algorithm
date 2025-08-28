import sys
sys.stdin = open("input.txt", "r")


n=int(input())
queue=[]
for _ in range(n):
    command=input().strip().split() # split()을 안하면, push 1이 하나의 문자열로 들어온다. strip()은 공백제거
    cmd=command[0]
    if cmd=='push':
        queue.append(command[1])
    elif cmd=='pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif cmd=='size':
        print(len(queue))
    elif cmd=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)

