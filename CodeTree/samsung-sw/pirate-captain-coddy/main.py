import sys
input = sys.stdin.readline
from collections import deque
import heapq

def attack_ready(pq, boats, args, time):
    n, *boat_infos = args
    
    for i in range(n):
        id, pi, ri = boat_infos[i * 3], boat_infos[i * 3 + 1], boat_infos[i * 3 + 2]
        heapq.heappush(pq, (-pi, id))
        boats[id] = (pi, ri, time)

def request_support(pq, boats, args, time):
    id, p, r = args
    heapq.heappush(pq, (-p, id))
    boats[id] = (p, r, time)

def repare_rocket(boats, pq, args):
    id, p = args
    boats[id] = (p, boats[id][1], boats[id][2])
    heapq.heappush(pq, (-p, id))

def order_attack(boats, curr_time, pq):
    sum_attack = 0
    count_attack_boat = 0
    attack_boat_number = []
    n = min(len(pq), 5)
    tmp = []
    while n > 0 and pq:
        priority, id = pq[0]
        start_time = boats[id][2]
        heapq.heappop(pq)
        if boats[id][0] != -priority:
            continue
        tmp.append((priority, id))
        if start_time > curr_time:
            continue

        sum_attack -= priority
        attack_boat_number.append(id)
        count_attack_boat += 1
        n -= 1
        boats[id] = (boats[id][0], boats[id][1], curr_time + boats[id][1])
    for priority, id in tmp:
        heapq.heappush(pq, (priority, id))
    print(sum_attack, len(attack_boat_number), *attack_boat_number)

def main():
    t = int(input())
    boats = {}
    pq = []
    for time in range(t):
        comm, *args = map(int, input().split())
        # print(pq)
        # print(time, " ", boats)
        match comm:
            case 100:
                attack_ready(pq, boats, args, time)
            case 200:
                request_support(pq, boats, args, time)
            case 300:
                repare_rocket(boats, pq, args)
            case 400:
                order_attack(boats, time, pq)

if __name__ == "__main__":
    main()