INF = float('inf')

n = int(input())
arr = list(map(int, input().split()))

size = 1
while size < n:
    size <<= 1
tree = [(INF, -1)] * (2 * size)
size -= 1


def update(idx, diff):
    idx += size
    tree[idx] = diff
    idx //= 2
    while idx:
        tree[idx] = min(tree[idx * 2], tree[idx * 2 + 1])
        idx //= 2


for i in range(n):
    update(i + 1, (arr[i], i + 1))


def search(left, right):
    left += size
    right += size
    ans = (INF, -1)

    while left <= right:
        if left % 2 == 1:
            ans = min(ans, tree[left])
            left += 1
        left //= 2

        if right % 2 == 0:
            ans = min(ans, tree[right])
            right -= 1
        right //= 2

    return ans[1]


m = int(input())
for i in range(m):
    command, h, k = map(int, input().split())
    if command == 1:
        update(h, (k, h))
    else:
        print(search(h, k))
