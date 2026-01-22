def solution(n, times):
    # 1. 탐색 범위 설정
    left = 1
    right = max(times) * n

    answer = right
    while left <= right:
        mid = (left + right) // 2

        # 2. mid분 동안 심사할 수 있는 총 인원 계산
        # 각 심사대마다 최대 몇 명을 심사 할 수 있는 지 판별
        total_people = 0
        for t in times:
            total_people += mid // t

            # 이미 n명을 넘었다면 더 계산할 필요 없음 (최적화)
            if total_people >= n:
                break

        # 3. 인원 수에 따라 범위 조절
        if total_people >= n:
            # n명 이상 심사 가능하다면, 시간이 남거나 딱 맞는 것
            # 더 짧은 시간 중에도 답이 있는지 확인하기 위해 범위를 좁힘
            answer = mid
            right = mid - 1
        else:
            # n명을 다 심사하지 못한다면, 시간이 더 필요함
            left = mid + 1

    return answer