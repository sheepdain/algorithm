from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    truck_weight_sum = 0
    while bridge:
        answer += 1
        out_truck = bridge.popleft()
        truck_weight_sum -= out_truck
        if truck:
            if truck_weight_sum + truck[0] <= weight:
                in_truck = truck.popleft()
                bridge.append(in_truck)
                truck_weight_sum +=in_truck
            else:
                bridge.append(0)
        if not truck and truck_weight_sum == 0:
            break

    return answer