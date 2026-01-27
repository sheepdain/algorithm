class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        answer = []
        ans = float('inf')
        arr.sort()
        for i in range(1, len(arr)):
            a, b = arr[i - 1], arr[i]
            if b - a < ans:
                ans = b - a
                answer = [[a, b]]
            elif b - a == ans:
                answer.append([a, b])
        return answer
        