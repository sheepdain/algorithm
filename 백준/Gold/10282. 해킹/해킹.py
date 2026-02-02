import heapq

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    hacking_list = [[] for _ in range(n + 1)]
    hacking_time = [float('inf') for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        hacking_list[b].append((a, s))

    hacking = []
    heapq.heappush(hacking,(0, c))

    while hacking:
        time, com_num = heapq.heappop(hacking)
        if hacking_time[com_num]>time:
            hacking_time[com_num] = time
            for h_com, h_time in hacking_list[com_num]:
                heapq.heappush(hacking, (time + h_time, h_com))

    ans_com_num, ans_time=0,0
    for ttt in hacking_time:
        if ttt!= float('inf'):
            ans_com_num+=1
            ans_time=max(ans_time, ttt)

    print(ans_com_num, ans_time)
