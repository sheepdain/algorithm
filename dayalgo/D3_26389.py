import sys

sys.stdin = open("input.txt", "r")

# T = int(input())
# for test_case in range(1, T + 1):
#     di = input()
#     ans = [False,False,False,False]
#     for d in di:
#         if d == "N":
#             if ans[0] == False:
#                 ans[0] = True
#         elif d == "S":
#             if ans[1] == False:
#                 ans[1] = True
#         elif d == "W":
#             if ans[2] == False:
#                 ans[2] = True
#         elif d == "E":
#             if ans[3] == False:
#                 ans[3] = True
#     ref = "Yes"
#     if ans[0] != ans[1]:
#         ref = "No"
#     if ans[2] != ans[3]:
#         ref = "No"
#     print(ref)

T = int(input())
for test_case in range(1, T + 1):
    di = input()
    ans = [False,False,False,False]
    if "N" in di:
        if ans[0] == False:
            ans[0] = True
    if "S" in di:
        if ans[1] == False:
            ans[1] = True
    if "W" in di:
        if ans[2] == False:
            ans[2] = True
    if "E" in di:
        if ans[3] == False:
            ans[3] = True
    ref = "Yes"
    if ans[0] != ans[1]:
        ref = "No"
    if ans[2] != ans[3]:
        ref = "No"
    print(ref)