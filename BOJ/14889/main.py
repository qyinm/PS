from itertools import combinations
import sys

input = sys.stdin.readline

def divide_equal_groups_unique(origin, k):
    result = []
    
    for comb in combinations(origin, k):
        group1 = list(comb)
        group2 = [x for x in origin if x not in group1]
        if group1[0] < group2[0]:
            result.append([group1, group2])
    
    return result

def calculate_group_sum(group_comb_list, graph):
    sum_group = 0
    for i in range(len(group_comb_list)):
        for j in range(len(group_comb_list)):
            if i != j:
                sum_group += graph[group_comb_list[i]-1][group_comb_list[j]-1]
    return sum_group

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

groups = divide_equal_groups_unique(range(1, n+1), n // 2)

answer = 10e9

for group1, group2 in groups:

    sum_g1 = calculate_group_sum(group1, graph)
    sum_g2 = calculate_group_sum(group2, graph)

    answer = min(answer, abs(sum_g1 - sum_g2))

print(answer)
