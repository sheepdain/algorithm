import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

tree = [None] * (4 * N)

def build(node, start, end):
    if start == end:
        tree[node] = (arr[start], arr[start])
        return

    mid = (start + end) // 2
    build(node*2, start, mid)
    build(node*2+1, mid+1, end)

    tree[node] = (
        min(tree[node*2][0], tree[node*2+1][0]),
        max(tree[node*2][1], tree[node*2+1][1])
    )

def query(node, start, end, left, right):
    if right < start or end < left:
        return (10**9, 0)

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    lmin, lmax = query(node*2, start, mid, left, right)
    rmin, rmax = query(node*2+1, mid+1, end, left, right)

    return (min(lmin, rmin), max(lmax, rmax))

build(1, 0, N-1)

for _ in range(M):
    a, b = map(int, input().split())
    mn, mx = query(1, 0, N-1, a-1, b-1)
    print(mn, mx)
