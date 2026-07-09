# import sys
#
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    st, ed = 0, len(string) - 1
    ans = 1
    while st < ed:
        if string[st] == string[ed]:
            st += 1
            ed -= 1
        else:
            ans = 0
            break
    print('#%d %d' % (test_case, ans))
