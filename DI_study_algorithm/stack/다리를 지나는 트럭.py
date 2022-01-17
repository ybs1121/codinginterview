def solution(bridge_length, weight, truck_weights):
    answer = 1
    pass_truck = []
    weight_now = 0
    bridge_on_truck = [0] * bridge_length
    while len(truck_weights) > 0:
        count = 0
        for i in range (0,bridge_length):
            answer += 1
            if weight_now <= weight:
                if len(truck_weights) > 1:
                    bridge_on_truck.append(truck_weights[count])
                    weight_now += truck_weights[count]
                    count += 1
                else:
                    bridge_on_truck.append(truck_weights[0])



        weight_now -= truck_weights[0]
        truck_weights.pop(0)
        bridge_on_truck.pop(0)

        print(truck_weights)
        print(answer)



    return answer


def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length

    while q:
        time += 1
        q.pop(0)
        print(q)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
        print(q)

    return time

if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights =[7,4,5,6]
    print(solution(bridge_length,weight,truck_weights))